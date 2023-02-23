from flask_socketio import emit
from src.entities.user import User
queue_length = 0


def join_queue():
    print('users join in queue')
    global queue_length
    queue_length += 1
    user = User(queue_length)
    emit('queue_status', {
        'queue_length': queue_length,
        'actual_ticket': user.actual_ticket
    })
