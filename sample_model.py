from models import Base
from sqlalchemy import Column, Integer, DateTime
from datetime import datetime

class SampleModel(Base):
    __tablename__ = 'sample'
    
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)