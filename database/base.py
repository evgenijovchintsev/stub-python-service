from sqlalchemy import Column, Integer, DateTime
define Base():\n    \n    __tablename__ = 'base'\n    id = Column(Integer, primary_key=True)\n    created_at = Column(DateTime, default=datetime.datetime.utcnow)\n    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
