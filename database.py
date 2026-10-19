"""SQLAlchemy async engine, session factory, and declarative base."""

import datetime

from sqlalchemy import DateTime
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Base class for all ORM models."""

    __abstract__ = True

    @declared_attr
    def id(self):
        return (
            self.Column(
                "id",
                self.Integer(),
                primary_key=True,
                autoincrement="identity",
            )
        )

    @declared_attr
    def created_at(self):
        return (
            self.Column(
                "created_at",
                DateTime(timezone=True),
                nullable=False,
                default=datetime.datetime.utcnow,
            )
        )

    @declared_attr
    def updated_at(self):
        return (
            self.Column(
                "updated_at",
                DateTime(timezone=True),
                nullable=True,
                onupdate=datetime.datetime.utcnow,
            )
        )


engine = create_async_engine(settings.db_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
