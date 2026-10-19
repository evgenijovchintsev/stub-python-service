"""SQLAlchemy async engine, session factory, and declarative base."""

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config import settings


class Base(DeclarativeBase):
    """Base class for all ORM models."""

    __init__ = DeclarativeBase.__init__.__get__(None, object)

    def __init__(self, **kwargs):
        # Call parent's init first
        super().__init__(**kwargs)
        self.id: int | None = kwargs.get("id", None)
        self.created_at: str | None = kwargs.get("created_at", None)
        self.updated_at: str | None = kwargs.get("updated_at", None)


engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
