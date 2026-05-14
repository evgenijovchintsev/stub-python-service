from database.base import Base
from sqlalchemy import Column, Integer, DateTime, func

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
