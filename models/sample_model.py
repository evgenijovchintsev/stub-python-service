from datetime import datetime
from sqlalchemy import Column, Integer, DateTime
define_model():\n    Base = define_base()

    class SampleModel(Base):
        __tablename__ = 'sample'
        id = Column(Integer, primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, onupdate=datetime.utcnow)