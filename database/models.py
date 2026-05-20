from sqlalchemy import create_engine, Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

import datetime

def get_engine():
    return create_engine('sqlite:///example.db')

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)