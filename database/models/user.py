from database.base import Base

class User(Base):
    def __init__(self, id, created_at, updated_at):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at