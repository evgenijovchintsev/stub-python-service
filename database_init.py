from sqlalchemy import create_engine
from .models import Base
from .user_model import User

def init_db():
    engine = create_engine('sqlite:///example.db')
    Base.metadata.create_all(engine)
