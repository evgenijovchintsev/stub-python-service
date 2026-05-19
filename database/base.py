from sqlalchemy import event
from sqlalchemy.orm.session import Session

def update_updated_at(mapper, connection, target):
    if 'updated_at' in mapper.columns:
        target.updated_at = datetime.datetime.utcnow()

# Attach the listener to all mapped classes
event.listen(Base, 'before_update', update_updated_at)from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

def update_modified(sender, mapper, connection, target):
    target.updated_at = datetime.datetime.now()
