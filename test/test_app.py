from src.app import socketio


def test_connection(app):
    flask_client = app.test_client()
    client_one = socketio.test_client(
        app=app,
        flask_test_client=flask_client
    )

    client_one.connect()
    assert client_one.is_connected() == True

    client_one.emit('ping')
    received = client_one.get_received()
    print(received)
    assert received[0]['name'] == 'pong'
