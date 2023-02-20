from flask import Flask
from flask_socketio import SocketIO
from os import environ

socketio = SocketIO()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
    socketio.init_app(app)

    import src.events
    return app
