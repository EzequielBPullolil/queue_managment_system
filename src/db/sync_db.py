from .models.queue import Queue
from src.db import Base, engine
import os


Base.metadata.create_all(engine)
