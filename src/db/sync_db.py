from .models import Queue, User, Queue_User
from src.db import Base, engine


Base.metadata.create_all(engine)
