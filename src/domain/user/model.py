from sqlalchemy import Column, String, Integer
from src.db import Base
from uuid_extensions import uuid7


class User(Base):
    __tablename__ = 'Users'

    id = Column(String(36), primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)

    def __init__(self, name, email, id):
        self.name = name
        self.email = email
        self.id = id

    def getId(self) -> int:
        return self.id
