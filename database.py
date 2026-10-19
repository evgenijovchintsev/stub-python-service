"""SQLAlchemy async engine, session factory, and declarative base."""

from datetime import timezone
from typing import Mapped

from sqlalchemy import DateTime as SQLDateTime
from sqlalchemy import Integer as SQLInteger
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column

from config import settings


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Declarative base for all ORM models."""


class BaseModel(Base):  # pylint: disable=too-few-public-methods
    """Abstract base class with common columns (id, created_at, updated_at) for all ORM models."""

    __abstract__ = True

    id: Mapped[SQLInteger] = mapped_column(primary_key=True, default=None)
    created_at: Mapped[SQLDateTime] = mapped_column(
        SQLDateTime(timezone=True),
        server_default=func.now(),
        default=lambda: func.now().astimezone(timezone.utc).replace(tzinfo=None),
    )
    updated_at: Mapped[SQLDateTime] = mapped_column(
        SQLDateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        default=lambda: func.now().astimezone(timezone.utc).replace(tzinfo=None),
    )


engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
