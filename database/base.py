from sqlalchemy.ext.declarative import declarative_base

def get_base():
    Base = declarative_base()
    return Base