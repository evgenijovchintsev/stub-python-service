"""SQLAlchemy async engine, session factory, and declarative base.
This module defines the Base ORM class with common columns (id, created_at, updated_at).
It also exposes an async SQLAlchemy engine and a sessionmaker.
"""

from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config import settings


class Base(DeclarativeBase):
    """Base class for all ORM models with id, created_at, updated_at."""
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime,
        onupdate=func.now(),
        server_default=func.now(),
        nullable=False,
    )  # pylint: disable=too-few-public-methods

# Engine and sessionmaker for async operations.
engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
