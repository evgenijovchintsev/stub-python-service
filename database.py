"""SQLAlchemy async engine, session factory, and declarative base."""

from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config import settings


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Base class for all ORM models."""

    __abstract__ = True

    def _generate_metadata_for_table(self, cls):
        super()._generate_metadata_for_table(cls)
        if not hasattr(cls, "_sa_columns"):
            return
        id_col_exists = any(
            (c.name == "id" and c.primary_key) for c in cls._sa_columns
        )
        created_at_exists = any(c.name == "created_at" for c in cls._sa_columns)
        updated_at_exists = any(c.name == "updated_at" for c in cls._sa_columns)
        if id_col_exists and not created_at_exists:
            cls.__table_args__.append(
                Column("created_at", DateTime(timezone=True), server_default="now()")
            )
        if id_col_exists and updated_at_exists and not created_at_exists:
            cls.__table_args__.append(
                Column("created_at", DateTime(timezone=True), server_default="now()")
            )
        elif not created_at_exists and not updated_at_exists:
            cls.__table_args__ += (
                Column("updated_at", DateTime(timezone=True), onupdate="now()"),
                Column("created_at", DateTime(timezone=True), server_default="now()"),
            )

    def _init_items(self):
        super()._init_items()
        self._generate_metadata_for_table(self)


engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
