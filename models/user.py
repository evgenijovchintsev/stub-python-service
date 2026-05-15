from sqlalchemy import Column, String
from database.base import BaseModel

class User(BaseModel):
    __tablename__ = 'users'
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)