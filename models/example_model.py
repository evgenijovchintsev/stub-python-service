from sqlalchemy import Column, Integer, DateTime
from database.base import Base
import datetime

class ExampleModel(Base):
    __tablename__ = 'example_models'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
