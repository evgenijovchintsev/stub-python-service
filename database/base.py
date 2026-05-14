from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime

def now():
    return datetime.utcnow()

Base = declarative_base()

class BaseModel:
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=now)
    updated_at = Column(DateTime, default=now, onupdate=now)