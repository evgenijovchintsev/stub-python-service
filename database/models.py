from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime
define_base():
    Base = declarative_base()
    
    class BaseModel(Base):
        __abstract__ = True
        id = Column(Integer, primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, onupdate=datetime.utcnow)
    return Base