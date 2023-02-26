import pytest
from src.app import create_app, socketio
from src.db import Session
from src.db.models import Queue, User
from uuid_extensions import uuid7

import src.db.sync_db


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        'TESTING': True
    })
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def sio(app):
    flask_client = app.test_client()
    sio = socketio.test_client(
        app=app,
        flask_test_client=flask_client
    )
    return sio


@pytest.fixture()
def queue_suject_id():
    session = Session()
    id = uuid7()
    queue = Queue(id=id, name='test_suject_queue')
    session.add(queue)
    session.commit()
    id = queue.id
    session.close()
    return id


@pytest.fixture()
def user_suject_id():
    session = Session()
    user = User(name='user_suject', email='test@test.com')
    session.add(user)
    session.commit()
    id = user.getId()
    session.close()

    return id
