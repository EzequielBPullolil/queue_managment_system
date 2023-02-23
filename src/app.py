from flask import Flask
from flask_socketio import SocketIO, emit
from os import environ
from src.events import join_queue
socketio = SocketIO(logger=True, engineio_logger=True)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
    socketio.init_app(app)

    @socketio.on('ping')
    def ping():
        emit('pong')

    socketio.on_event('join_queue', join_queue)

    return app
