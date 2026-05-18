from sqlalchemy import create_engine, Column, Integer, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def get_db_engine():
    engine = create_engine('sqlite:///./sqlalchemy_example.db')
    return engine

Base = declarative_base()
