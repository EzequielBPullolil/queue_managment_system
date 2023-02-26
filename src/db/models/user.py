from sqlalchemy import Column, String, Integer
from src.db import Base


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def getId(self) -> int:
        return self.id
