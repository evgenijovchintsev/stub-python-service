from sqlalchemy.ext.declarative import declarative_base
from database.base import Base


class ExampleModel(Base):
    __tablename__ = 'example'
    
    name = Column(String(50))
    description = Column(Text)