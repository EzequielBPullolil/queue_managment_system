from sqlalchemy import select
from flask_socketio import emit
# infrastructure imports
from src.db import Session
# domain imports
from .model import Queue_User
from src.app import socketio
from .exceptions import NonQueuedUser


def join_queue(data):
    '''
        Persist queue_user using user_id and queue_id 
        and emits event 'increment_queue_length'
    '''
    user_ticket = 1
    user_id = data['user_id']
    queue_id = data['queue_id']
    session = Session()

    response = session.execute(
        select(Queue_User.user_ticket).where(Queue_User.queue_id ==
                                             queue_id).order_by(Queue_User.user_ticket.asc())
    ).fetchall()

    if (len(response) > 0):
        user_ticket = response[0][0] + 1

    queue_user = Queue_User(
        user_id=user_id, queue_id=queue_id, user_ticket=user_ticket
    )
    session.add(queue_user)
    session.commit()
    session.close()

    print(f"user with id[{user_id}] queued with queue [{queue_id}]")
    emit('increment_queue_length', queue_id)
    emit('user_ticket', user_ticket)


def leave_queue(data):
    '''
        Delete queue_user row they have the same queue_id 
        and user_id 

    '''
    user_id = data['user_id']
    queue_id = data['queue_id']
    try:
        session = Session()
        queue_user = session.execute(
            select(Queue_User).where(Queue_User.user_id ==
                                     user_id, Queue_User.queue_id == queue_id)
        ).fetchone()[0]

        session.delete(queue_user)
        session.commit()
        session.close()
    except TypeError:
        raise NonQueuedUser(queue_id=queue_id, user_id=user_id)

    socketio.emit('decrement_queue_length', queue_id)
