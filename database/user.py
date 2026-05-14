from sqlalchemy import Column, String
from .models import Base
class User(Base):
    __tablename__ = 'users'
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)