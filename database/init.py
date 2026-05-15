from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.base import Base, BaseModel

gine = create_engine('sqlite:///example.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)