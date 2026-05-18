# models/comment.py
from database.base import Base, Column, Integer, DateTime, get_current_time

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=get_current_time)
    updated_at = Column(DateTime, onupdate=get_current_time)