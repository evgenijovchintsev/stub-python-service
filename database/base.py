from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

def create_time():
    return datetime.utcnow()

class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=create_time)
    updated_at = Column(DateTime, default=create_time, onupdate=datetime.utcnow)