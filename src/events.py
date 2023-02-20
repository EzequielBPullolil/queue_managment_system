from .app import socketio
from flask_socketio import emit


@socketio.on('ping')
def connect():
    emit('pong')
