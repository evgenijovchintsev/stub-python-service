"""SQLAlchemy async engine, session factory, and declarative base."""

import datetime as dt
from sqlalchemy import DateTime, Integer, func
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config import settings


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Base class for all ORM models."""

    __abstract__ = True


def get_base_model(name: str) -> type[dt.datetime]:
    """Create a new model inheriting from Base with default columns."""

    class BaseModel(Base):  # pylint: disable=too-few-public-methods
        """Base model with standard fields (id, created_at, updated_at)."""

        __tablename__ = f"{name.lower()}" if name else "base"

        id: Mapped[int] = mapped_column(Integer, primary_key=True)
        created_at: Mapped[dt.datetime | None] = mapped_column(
            DateTime(timezone=True), server_default=func.now(), nullable=False
        )
        updated_at: Mapped[dt.datetime | None] = mapped_column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
            nullable=False,
        )

    return BaseModel


engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
