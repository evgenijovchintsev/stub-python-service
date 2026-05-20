from .base import BaseModel
from sqlalchemy import Column, String

class User(BaseModel):
    username = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
