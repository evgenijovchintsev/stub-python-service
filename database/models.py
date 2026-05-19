from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

def utc_now():
    return datetime.datetime.utcnow()

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=utc_now)
    updated_at = Column(DateTime, default=utc_now, onupdate=utc_now)