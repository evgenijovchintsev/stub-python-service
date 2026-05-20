from sqlalchemy import Column, Integer, DateTime
from datetime import datetime
class Base():
    __tablename__ = 'base'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)