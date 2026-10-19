from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

declarative_base = declarative_base()

Base = declarative_base()

def add_created_updated_at(model):
    model.created_at = Column(DateTime(timezone=True), server_default=func.now())
    model.updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())