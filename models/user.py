# models/user.py
from database.base import Base, Column, Integer, DateTime, get_current_time

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=get_current_time)
    updated_at = Column(DateTime, onupdate=get_current_time)