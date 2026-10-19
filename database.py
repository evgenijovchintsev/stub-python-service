"""SQLAlchemy async engine, session factory, and declarative base."""

import datetime as dt

from sqlalchemy import DateTime
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config import settings


class TimestampMixin:  # pylint: disable=too-few-public-methods
    """Mixin for automatic timestamp tracking."""

    created_at: Mapped[dt.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=dt.func.now(),
    )
    updated_at: Mapped[dt.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=dt.func.now(),
        onupdate=dt.func.now(),
    )


class Base(DeclarativeBase, TimestampMixin):  # pylint: disable=too-few-public-methods
    """Base class for all ORM models."""


engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
