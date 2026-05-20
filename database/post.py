from sqlalchemy import Column, Integer, String, DateTime, func
from .models import get_declarative_base
class Post(get_declarative_base()):
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), default=func.now())