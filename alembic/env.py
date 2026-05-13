"""Environment configuration for Alembic migrations.

This script sets up the migration context, using database URL from the application
settings and configuring target metadata for autogeneration if available.
"""

from __future__ import annotations

import os
from logging.config import fileConfig

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

# Alembic imports
from alembic import context

# Import application settings to get DB URL
try:
    from config import settings  # type: ignore
except Exception as exc:  # pragma: no cover - safety net for missing config
    raise RuntimeError("Failed to import application settings") from exc

# Try importing the application's SQLAlchemy metadata if it exists.
# This is optional; migrations can still run without it until models are added.
try:
    # Common pattern: models module defines Base = declarative_base()
    from models import Base  # type: ignore
    target_metadata = Base.metadata  # pragma: no cover - depends on future code
except Exception:  # noqa: BLE001
    target_metadata = None

# Alembic configuration instance
config = context.config

# If a config file is provided, use it for logging setup.
if config.config_file_name:
    fileConfig(config.config_file_name)

# Set the SQLAlchemy URL in Alembic's config if not already set.
# This ensures that ``alembic upgrade`` works even when the environment variable
# is only present in the application settings.
config.set_main_option("sqlalchemy.url", settings.db_url)


def run_migrations_offline() -> None:
    """Run migrations in offline mode.

    This generates SQL scripts without requiring a database connection.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in online mode.

    This connects to the database using the URL from settings and applies
    any pending migration scripts.
    """
    connectable: Engine = create_engine(settings.db_url, poolclass=None)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

# Choose mode based on Alembic's context.
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()