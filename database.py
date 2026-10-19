"""SQLAlchemy async engine, session factory, and declarative base."""

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config import settings


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Base class for all ORM models."""

    __table_args__ = {"sqlite_autoincrement": True}

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    created_at = sa.Column(
        sa.TIMESTAMP(), server_default=sa.func.now(), nullable=False
    )
    updated_at = sa.Column(
        sa.TIMESTAMP(), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False
    )


engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
