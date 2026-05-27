# SQLAlchemy ORM models

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func
from database import Base

class BaseMixin:
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.current_timestamp(), nullable=False)