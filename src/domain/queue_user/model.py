from sqlalchemy import Column, ForeignKey, Integer
from src.db import Base


class Queue_User(Base):
    __tablename__ = 'queue_user'

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

    user_ticket = Column(
        Integer
    )

    def __repr__(self):
        return f"QueueUser(queued_id={self.queue_id}, user_id={self.user_id}, user_ticket={self.user_ticket})"

    def __init__(self, queue_id, user_id, user_ticket):
        self.queue_id = queue_id
        self.user_id = user_id
        self.user_ticket = user_ticket

    def as_dict(self):
        return {
            c.name: getattr(self, c.name) for c in self.__table__.columns
        }
