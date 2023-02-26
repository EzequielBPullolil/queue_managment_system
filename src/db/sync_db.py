from src.domain.user.model import User
from src.domain.queue.model import Queue
from src.domain.queue_user.model import Queue_User
from src.db import Base, engine


Base.metadata.create_all(engine)
