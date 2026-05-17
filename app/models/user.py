from database.base import BaseModel as Base

class User(Base):
    __tablename__ = 'users'
    username = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False)