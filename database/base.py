# Base class for ORM models
from sqlalchemy.ext.declarative import declarative_base

def timestamp():
    from datetime import datetime
    return datetime.utcnow()

Base = declarative_base()