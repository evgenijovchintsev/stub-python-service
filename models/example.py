from database.base import Base
from sqlalchemy import Column, Integer, String, Text


class ExampleModel(Base):
    __tablename__ = 'example'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), default=Base.get_current_time())
    updated_at = Column(DateTime(timezone=True), onupdate=Base.get_current_time())
    name = Column(String(255))
    description = Column(Text)