from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime
import datetime

def get_current_time():
    return datetime.datetime.utcnow()

Base = declarative_base()