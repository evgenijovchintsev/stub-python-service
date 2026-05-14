# Import necessary modules from SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime
import datetime

def utcnow():
    return datetime.datetime.utcnow()

# Create the Base class
Base = declarative_base()