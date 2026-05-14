from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

def created_at_default(context):
    return context.current_parameters['created_at'] or datetime.utcnow()

def updated_at_default(context):
    return context.current_parameters['updated_at'] or datetime.utcnow()

def update_updated_at(mapper, connection, target):
    target.updated_at = datetime.utcnow()

Base = declarative_base()

Base.metadata.create_all()
