"""SQLAlchemy async engine, session factory, and declarative base."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config import settings


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Base class for all ORM models."""

    class User(Base):
        __tablename__ = "users"

        id: Mapped[int] = mapped_column(Integer, primary_key=True)
        name: Mapped[str] = mapped_column(String(100), nullable=False)
        email: Mapped[str] = mapped_column(String(255), nullable=False)


engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
