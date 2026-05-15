
def get_utcnow():
    return datetime.datetime.utcnow()from database.base import Base
from sqlalchemy import Column, Integer, DateTime, String
import datetimefrom database.base import Base
from sqlalchemy import Column, Integer, String, DateTime
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=get_utcnow)
    updated_at = Column(DateTime, onupdate=get_utcnow)