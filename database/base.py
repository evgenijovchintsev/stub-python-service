# Base class for ORM models
from sqlalchemy import Column, Integer, DateTime
def timestamp():
    from datetime import datetime
    return datetime.utcnow()
class BaseMixin:
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), default=timestamp, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=timestamp, onupdate=timestamp, nullable=False)