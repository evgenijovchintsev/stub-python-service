from sqlalchemy import create_engine, Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

def init_db():
    engine = create_engine('sqlite:///example.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()