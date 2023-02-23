from flask_socketio import emit

queue_length = 0


def join_queue():
    print('users join in queue')
    global queue
    queue += 1
    emit('queue_status', {
        'queue_length': queue_length,
        'actual_ticket': 99
    })
