from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, **kwargs):
        super(BaseModel, self).__init__(**kwargs)
        self.updated_at = datetime.datetime.utcnow()