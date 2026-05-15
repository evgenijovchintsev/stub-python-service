from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

def get_current_time():
    return datetime.utcnow()

Base = declarative_base()

class BaseMixin:
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=get_current_time, nullable=False)
    updated_at = Column(DateTime, default=get_current_time, onupdate=get_current_time, nullable=False)