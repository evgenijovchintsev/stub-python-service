from database.base import Base, BaseMixin

class User(BaseMixin, Base):
    __tablename__ = 'users'

    # Add other columns as needed