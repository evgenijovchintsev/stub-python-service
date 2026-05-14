from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

declarative_base()

def timestamp():
    return datetime.utcnow()

class Base(object):
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=timestamp)
    updated_at = Column(DateTime, default=timestamp, onupdate=timestamp)