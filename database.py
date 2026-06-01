"""SQLAlchemy async engine, session factory, and declarative base."""

import datetime

from sqlalchemy import DateTime, Integer
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config import settings


class TimestampMixin:  # pylint: disable=too-few-public-methods
    """Mix-in for automatic timestamp columns."""

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.datetime.now
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.datetime.now, onupdate=datetime.datetime.now
    )


class Base(TimestampMixin, DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Base class for all ORM models."""


engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
