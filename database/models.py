from sqlalchemy import func
from sqlalchemy import Column, Integer, DateTime, func


class Base:
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now(), default=func.now())