
from flask_socketio import emit
# infrastructure imports
from src.db import Session
# domain imports
from .model import Queue_User


def join_queue(data):
    '''
        Persist queue_user using user_id and queue_id 
        and emits event 'increment_queue_length'
    '''
    user_id = data['user_id']
    queue_id = data['queue_id']
    session = Session()

    queue_user = Queue_User(user_id=user_id, queue_id=queue_id)

    session.add(queue_user)
    session.commit()

    emit('increment_queue_length', queue_id)

    session.close()
