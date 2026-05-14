from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

declarative_base()
Base = declarative_base()

class BaseMixin(object):
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    @classmethod
    def __declare_last__(cls):
        for column in cls.__table__.columns:
            if isinstance(column.default, datetime.datetime.utcnow):
                column.onupdate = datetime.datetime.utcnow