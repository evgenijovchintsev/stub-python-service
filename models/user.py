from sqlalchemy import String
from database.base import Base
class User(Base):
    __tablename__ = 'users'
    name = Column(String)
    email = Column(String)