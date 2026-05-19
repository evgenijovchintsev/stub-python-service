from .models import Base
from sqlalchemy import Column, String

class User(Base):
    __tablename__ = 'users'
    name = Column(String)
    email = Column(String)