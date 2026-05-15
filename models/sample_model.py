from database.base import Base
from sqlalchemy import Column, String

class SampleModel(Base):
    __tablename__ = 'sample_models'
    name = Column(String(50), nullable=False)
