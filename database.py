"""SQLAlchemy async engine, session factory, and declarative base."""

import datetime
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config import settings


class TimestampsMixin:
    """Миксин для автоматического создания и обновления временных меток."""

    created_at: datetime.datetime = Column(
        DateTime(timezone=True), default=datetime.datetime.now, nullable=False
    )
    updated_at: datetime.datetime = Column(
        DateTime(timezone=True),
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
        nullable=False,
    )


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Базовый класс для всех ORM моделей."""

    id: int = Column(Integer, primary_key=True, autoincrement=True)


engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
