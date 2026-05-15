from database.base import Base
from sqlalchemy import Column, Integer, String, DateTime


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=)
    updated_at = Column(DateTime(timezone=True), onupdate=)
