# Create the Base class
Base = declarative_base()

# Define a base model with common fields
class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=utcnow)
    updated_at = Column(DateTime, onupdate=utcnow)# Import necessary modules from SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, DateTime
import datetime

def utcnow():
    return datetime.datetime.utcnow()

# Create the Base class
Base = declarative_base()