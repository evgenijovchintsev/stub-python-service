"""Base ORM model with common columns and SQLAlchemy async configuration.

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped
import uuid
from sqlalchemy.sql import func

from config import settings

class Base(DeclarativeBase):
    """Base class for all ORM models."""
    id: Mapped[uuid.UUID] = Mapped(uuid.uuid4, primary_key=True)
    created_at: Mapped[str | None] = Mapped(func.now(), nullable=False, server_default=func.now())
    updated_at: Mapped[str | None] = Mapped(func.now(), nullable=False, onupdate=func.now(), server_default=func.now())

engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
