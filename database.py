"""SQLAlchemy async engine, session factory, and declarative base."""

import datetime as dt
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.func import now as sql_now
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import func

from config import settings


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Base class for all ORM models."""

    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), nullable=False, default=dt.datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), nullable=False, default=sql_now(func.now()))


engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
