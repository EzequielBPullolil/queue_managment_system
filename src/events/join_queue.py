from flask_socketio import emit


def join_queue():
    print('users join in queue')
    emit('queue_status', {
        'queue_length': 100,
        'actual_ticket': 99
    })
