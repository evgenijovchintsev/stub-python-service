"""SQLAlchemy async engine, session factory, and declarative base."""

import datetime

from sqlalchemy import DateTime, Integer
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, declared_attr

from config import settings


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Base class for all ORM models."""

    id = None
    created_at = None
    updated_at = None

    @declared_attr
    def __tablename__(self):
        return self.__name__.lower()

    @declared_attr
    def id(self):
        return Integer(primary_key=True)

    @declared_attr
    def created_at(self):
        return DateTime(timezone=True, default=datetime.datetime.now, onupdate=None)

    @declared_attr
    def updated_at(self):
        return DateTime(timezone=True, default=datetime.datetime.now, onupdate=datetime.datetime.now)


engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
