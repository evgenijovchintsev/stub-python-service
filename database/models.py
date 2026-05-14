from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

def created_at_default(context):
    return context.current_parameters['created_at'] or datetime.utcnow()

def updated_at_default(context):
    return context.current_parameters['updated_at'] or datetime.utcnow()

def update_updated_at(mapper, connection, target):
    target.updated_at = datetime.utcnow()

class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=created_at_default)
    updated_at = Column(DateTime, default=updated_at_default, onupdate=datetime.utcnow)

Base = declarative_base()