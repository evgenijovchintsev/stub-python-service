from sqlalchemy import create_engine, Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

def get_db_url():
    return "sqlite:///./test.db"

engine = create_engine(get_db_url(), connect_args={"check_same_thread": False})
Base = declarative_base()

# Example of a simple model using Base
class SampleModel(Base):
    __tablename__ = 'sample'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
