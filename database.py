"""SQLAlchemy async engine, session factory, and declarative base."""

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, DateTime, func, text
from config import settings


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Base class for all ORM models.

    Provides common columns:
    - ``id`` as an auto‑increment primary key.
    - ``created_at`` timestamp set at insert time.
    - ``updated_at`` timestamp updated on every change.
    """

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), server_default=text('now()'), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=text('now()'),
        onupdate=func.now(),
        nullable=False,
    )


engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
