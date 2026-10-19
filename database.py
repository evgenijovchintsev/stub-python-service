"""SQLAlchemy async engine, session factory, and declarative base."""

from sqlalchemy import Column, DateTime, event
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config import settings
from sqlalchemy.ext.declarative import declared_attr


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Base class for all ORM models."""
    __abstract__ = True

    @declared_attr
    def id(cls):
        return Column(
            "id",
            primary_key=True,
            autoincrement=True,
            nullable=False,
        )

    @declared_attr
    def created_at(cls):
        return Column(
            "created_at",
            DateTime(timezone=True),
            server_default=Column("NOW()"),
            nullable=False,
        )

    @declared_attr
    def updated_at(cls):
        return Column(
            "updated_at",
            DateTime(timezone=True),
            onupdate=on_update(),
            server_default=Column("NOW()"),
            nullable=False,
        )


@event.listens_for(Base, "after_insert")  # pylint: disable=no-member
def receive_after_insert(model, conn):
    if hasattr(model, "updated_at"):
        now = model.__table__.columns["updated_at"]
        if now.onupdate is not None:
            conn.execute(now.onupdate._generate())


def on_update():
    from sqlalchemy import func

    return func.now()


engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
