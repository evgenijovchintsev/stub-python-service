from database.base import Base\nfrom sqlalchemy import Column, String

class User(Base):\n    __tablename__ = 'users'\n    username = Column(String(80), unique=True, nullable=False)
