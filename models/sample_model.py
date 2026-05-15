from sqlalchemy import Column, Integer, DateTime, func
from .models import Base

class SampleModel(Base):
    __tablename__ = 'sample'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())