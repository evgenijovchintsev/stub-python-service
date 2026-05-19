# This is a generated file. Do not modify manually.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime
from datetime import datetime

def utcnow():
    return datetime.utcnow()

class Base(declarative_base()):
    __abstract__ = True
    
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), default=utcnow)
    updated_at = Column(DateTime(timezone=True), default=utcnow, onupdate=utcnow)