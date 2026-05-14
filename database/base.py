from sqlalchemy import Column, Stringfrom sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

def get_current_time():
    return datetime.datetime.utcnow()

Base = declarative_base()

class BaseMixin:
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=get_current_time)
    updated_at = Column(DateTime, onupdate=get_current_time)
