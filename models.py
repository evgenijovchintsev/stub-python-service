from base import BaseModel
from sqlalchemy import String

class User(BaseModel):
    __tablename__ = 'users'

    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)