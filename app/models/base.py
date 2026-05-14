from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy import Column, Integer, DateTime

Base = declarative_base()

class CommonFieldsMixin(object):
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)