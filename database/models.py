from sqlalchemy import create_engine, Column, Integer, DateTime
from datetime import datetime
define_base():
    from sqlalchemy.ext.declarative import declarative_base
    Base = declarative_base()
    class CustomBase(Base):
        __abstract__ = True
        id = Column(Integer, primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, onupdate=datetime.utcnow)
    return CustomBase