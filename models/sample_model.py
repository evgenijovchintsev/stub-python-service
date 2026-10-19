from database.base import Base

class SampleModel(Base):
    __tablename__ = 'sample_models'

    id = Column(Integer, primary_key=True)

    def __init__(self):
        add_created_updated_at(self)