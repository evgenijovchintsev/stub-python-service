# database/base.py
from sqlalchemy.ext.declarative import declarative_base
import datetime
def now():
    return datetime.datetime.utcnow()

Base = declarative_base()
class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=now())
    updated_at = Column(DateTime, onupdate=now())