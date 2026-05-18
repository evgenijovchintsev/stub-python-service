from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime
import datetime

def init_db():
    Base.metadata.create_all(bind=engine)"""SQLAlchemy async engine, session factory, and declarative base."""

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config import settings

Base = declarative_base()
class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Base class for all ORM models."""
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)

engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)