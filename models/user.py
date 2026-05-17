from .base import Base
from sqlalchemy import Column, String

class User(Base):
    __tablename__ = 'users'
    username = Column(String(50), unique=True)
    email = Column(String(120), unique=True)