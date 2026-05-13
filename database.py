"""SQLAlchemy async engine, session factory, and declarative base."""

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config import settings


from sqlalchemy.orm import declared_attr
from sqlalchemy import Column, Integer, DateTime, func

class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Base class for all ORM models. Provides id, created_at, and updated_at columns."""

    @declared_attr.directive
    def id(cls):
        return Column(Integer, primary_key=True)

    @declared_attr.directive
    def created_at(cls):
        return Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    @declared_attr.directive
    def updated_at(cls):
        return Column(
            DateTime(timezone=True),
            default=func.now(),
            onupdate=func.now(),
            nullable=False,
        )


engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
