"""SQLAlchemy async engine, session factory, and declarative base."""

from sqlalchemy import DateTime, Integer
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config import settings


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Base class for all ORM models."""

    __abstract__ = True

    id = Integer()
    created_at = DateTime(timezone=True, server_default="NOW()")
    updated_at = DateTime(timezone=True, onupdate="NOW()", server_default="NOW()")


engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
