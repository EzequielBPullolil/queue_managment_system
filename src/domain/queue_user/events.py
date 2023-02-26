from sqlalchemy import select
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


def leave_queue(data):
    '''
        Delete queue_user row they have the same queue_id 
        and user_id 

    '''
    user_id = data['user_id']
    queue_id = data['queue_id']
    session = Session()

    queue_user = session.execute(
        select(Queue_User).where(Queue_User.user_id ==
                                 user_id, Queue_User.queue_id == queue_id)
    ).fetchone()[0]

    # print(queue_user)
    session.delete(queue_user)
    # print('deleted queue_user')
    session.commit()

    emit('decrement_queue', queue_id)
