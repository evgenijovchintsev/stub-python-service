from database.base import Base, BaseMixin


class User(Base, BaseMixin):
    __tablename__ = 'users'
    username = Column(String(50), unique=True)
