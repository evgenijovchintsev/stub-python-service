from sqlalchemy import Column, Integer, DateTime, func

class Base:
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now(), server_default=func.now())

# Example of a model inheriting from Base
class User(Base):
    __tablename__ = 'users'
    username = Column(String(80), unique=True, nullable=False)
