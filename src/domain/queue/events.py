from sqlalchemy import select
# insfrastructure imports
from src.db import Session
# domain imports
from .model import Queue


def increment_queue_length(queue_id):
    '''
        Finds queue by id and 
        imcrement they queue_length by 1
    '''
    session = Session()

    queue = session.execute(
        select(Queue).where(Queue.id == queue_id)
    ).fetchone()[0]

    queue.incrementLength()
