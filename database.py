"""SQLAlchemy async engine, session factory, and declarative base."""

from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, Integer, Column, String
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped

from config import settings


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Base class for all ORM models."""

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    created_at: Mapped[datetime] = Column(
        DateTime(timezone=True), server_default=datetime.now()
    )
    updated_at: Optional[datetime] = Column(DateTime(timezone=True), nullable=True)

    @declared_attr
    def __table_args__(self):
        return (
            {"sqlite_autoincrement": True},
        )


engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
