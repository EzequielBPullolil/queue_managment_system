from sqlalchemy import Column, String
from src.db import Base


class Queue(Base):
    __tablename__ = 'Queues'

    id = Column(String(36), primary_key=True)
    name = Column(String(50), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name
