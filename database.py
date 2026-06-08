"""SQLAlchemy async engine, session factory, and declarative base."""

from sqlalchemy import Column, DateTime, Integer, Text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from config import settings


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Base class for all ORM models.
    
    All models that inherit from this base will automatically get:
    - id (integer primary key)
    - created_at (datetime, auto-filled on insert)
    - updated_at (datetime, auto-updated on row updates)
    """
    
    __table_args__ = (
        {
            "sqlite_autoincrement": True,
        },
    )

    id = Column(Integer, primary_key=True, index=True, comment="Unique identifier")
    created_at = Column(
        DateTime(timezone=True),
        default=lambda: Text('now()'),
        comment="Record creation timestamp"
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: Text('now()'),
        onupdate=lambda: Text('now()'),
        comment="Last record update timestamp"
    )


engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
