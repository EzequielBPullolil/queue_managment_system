from sqlalchemy import Column, ForeignKey, Integer
from src.db import Base


class Queue_User(Base):
    __tablename__ = 'Queues_Users'

    queue_id = Column(
        'queue_id',
        ForeignKey('Queues.id'),
        primary_key=True
    )
    user_id = Column(
        'user_id',
        ForeignKey('Users.id'),
        primary_key=True
    )

    def __init__(self, id, name):
        self.id = id
        self.name = name
