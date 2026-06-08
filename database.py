"""SQLAlchemy async engine, session factory, and declarative base."""

from sqlalchemy import Column, DateTime
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql.functions import now as sql_now

from config import settings


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Base class for all ORM models."""

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=sql_now(),
        init=False,
        nullable=False,
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=sql_now(),
        onupdate=sql_now(),
        init=False,
        nullable=False,
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=sql_now(),
        init=False,
        nullable=False,
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=sql_now(),
        onupdate=sql_now(),
        init=False,
        nullable=False,
    )


engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
