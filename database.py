"""SQLAlchemy async engine, session factory, and declarative base."""

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config import settings


from sqlalchemy import Column, Integer, DateTime, func

class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Base class for all ORM models.

    Provides common columns:
    - ``id`` (primary key)
    - ``created_at`` timestamp set on insert
    - ``updated_at`` timestamp updated on each change.
    """
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)


engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
