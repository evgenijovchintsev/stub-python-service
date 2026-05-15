from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

declare_base = declarative_base()


class Base(declare_base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())