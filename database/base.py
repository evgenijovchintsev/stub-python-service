# database/base.py

from sqlalchemy.ext.declarative import declarative_base
import datetime

def get_current_time():
    return datetime.datetime.utcnow()

Base = declarative_base()