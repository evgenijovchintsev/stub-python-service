from sqlalchemy import Column, Integer, String, DateTime, func
from .models import get_declarative_base
class User(get_declarative_base()):
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), default=func.now())