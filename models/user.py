from database.base import Base
from sqlalchemy import Column, String
class User(Base):
    __tablename__ = 'users'
    username = Column(String(80), unique=True, nullable=False)