"""SQLAlchemy async engine, session factory, and declarative base."""

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, declared_attr

from config import settings


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Base class for all ORM models."""

    if sa.__version__.startswith("2"):
        __table_args__ = {"extend_existing": True}

    @declared_attr
    def id(self):
        return sa.Column(
            "id", sa.Integer, primary_key=True, autoincrement=True
        )

    @declared_attr
    def created_at(self):
        return sa.Column("created_at", sa.DateTime, nullable=True)

    @declared_attr
    def updated_at(self):
        from sqlalchemy import func

        return sa.Column(
            "updated_at", sa.DateTime, nullable=True, onupdate=func.now()
        )


engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
