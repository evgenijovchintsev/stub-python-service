"""SQLAlchemy async engine, session factory, and declarative base."""

from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, func
from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Base class for all ORM models."""

    @declared_attr.directive
    def __table_args__(self):
        return {"extend_existing": True}

    id = Column(Integer, primary_key=True)


def init_model(cls):
    if not hasattr(cls, "created_at"):
        cls.created_at = Column(DateTime(timezone=True), default=func.now())
    if not hasattr(cls, "updated_at"):
        cls.updated_at = Column(
            DateTime(timezone=True), onupdate=datetime.utcnow


def get_model_bases(base):
    return (base,) + Base.__bases__ if base is not None else ()
