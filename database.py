"""SQLAlchemy async engine, session factory, and declarative base."""
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config import settings


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Base class for all ORM models."""

    __table_args__ = {
        "sa_pool_pre_ping": True,
    }

    id: Mapped[int] = sa.Column(sa.Integer, primary_key=True, nullable=False)
    created_at: Mapped[datetime] = sa.Column(
        sa.DateTime(timezone=True),
        default=datetime.now,
        nullable=False,
        index=True,
    )
    updated_at: Mapped[datetime] = sa.Column(
        sa.DateTime(timezone=True),
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
        index=True,
    )


engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
