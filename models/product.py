from sqlalchemy import String
from database.base import Base
class Product(Base):
    __tablename__ = 'products'
    name = Column(String)
    price = Column(Integer)