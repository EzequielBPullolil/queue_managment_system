from src.app import socketio


def test_ping_pong(sio):
    '''
        sio test client connect app and 
        try to emit PING and assert if 
        they received PONG event
    '''
    sio.connect()
    assert sio.is_connected() == True

    sio.emit('ping')
    received = sio.get_received()
    assert len(received) > 0
    assert received[0]['name'] == 'pong'
    sio.disconnect()


def test_join_queue(app):
    flask_client = app.test_client()
    client1 = socketio.test_client(
        app=app,
        flask_test_client=flask_client
    )
    client1.connect()
    assert client1.is_connected() == True

    client1.emit('join_queue')

    received = client1.get_received()
    queue_status = received[0]
    assert queue_status['name'] == 'queue_status'
    assert queue_status['args'][0] == {
        'queue_length': 100, 'actual_ticket': 99}
