from sqlalchemy import Column, String, Integer
from src.db import Base


class Queue(Base):
    __tablename__ = 'Queues'

    id = Column(String(36), primary_key=True)
    name = Column(String(50), nullable=False)
    queue_length = Column(Integer, default=0)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"Queue(id={self.id!r}, name={self.name!r}, queue_length={self.queue_length!r})"
