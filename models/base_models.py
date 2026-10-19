"""
Base model classes with common fields for ORM entities.

Provides:
- BaseModel: inherits from Base, adds id (int, primary key)
- BaseModelTimestamped: inherits from BaseModel, adds created_at and updated_at timestamps

All models should inherit from BaseModelTimestamped.
"""

from datetime import datetime
from sqlalchemy import DateTime, Integer, Column
from database import Base as ORMBase


class BaseModel(ORMBase):
    """Base model with id field."""

    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)


class BaseModelTimestamped(BaseModel):
    """Base model with timestamps."""

    __abstract__ = True

    created_at = Column(
        DateTime(timezone=True), default=datetime.utcnow
    )
    updated_at = Column(
        DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow
    )