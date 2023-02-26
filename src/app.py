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

    from src.domain.queue.route import queue_bp
    from src.domain.queue.events import increment_queue_length
    socketio.on_event('increment_queue_length', increment_queue_length)
    app.register_blueprint(queue_bp)

    from src.domain.queue_user.events import join_queue
    socketio.on_event('join_queue', join_queue)
    return app
