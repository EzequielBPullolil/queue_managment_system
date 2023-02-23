from flask import Flask
from flask_socketio import SocketIO, emit
from os import environ

socketio = SocketIO(logger=True, engineio_logger=True)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
    socketio.init_app(app)

    @socketio.on('ping')
    def ping():
        emit('pong')

    @socketio.on('join_queue')
    def join_queue():
        print('joinend in queue')
        emit('queue_status', {
            'queue_length': 100,
            'actual_ticket': 99
        })

    return app
