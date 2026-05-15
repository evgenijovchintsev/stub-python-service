from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

def timestamp():
    return datetime.utcnow()

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=timestamp)
    updated_at = Column(DateTime, default=timestamp, onupdate=timestamp)