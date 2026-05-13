from datetime import datetime
import uuid

from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """Abstract base class for all ORM models with common fields."""
    __abstract__ = True

    id: str = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
    created_at: datetime = Column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    updated_at: datetime = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
