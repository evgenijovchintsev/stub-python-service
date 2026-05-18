from database.models import BaseModel
from datetime import datetime
from database.models import BaseModel
from sqlalchemy import String

class User(BaseModel):
    __tablename__ = 'users'
    username = Column(String, unique=True, index=True)
