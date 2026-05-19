from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

def update_modified(sender, mapper, connection, target):
    target.updated_at = datetime.datetime.now()
