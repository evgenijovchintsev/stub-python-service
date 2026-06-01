"""SQLAlchemy async engine, session factory, and declarative base."""

import sqlalchemy as sa
from sqlalchemy import DateTime, func
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config import settings


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Base class for all ORM models."""

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[sa.DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[sa.DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )


engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
