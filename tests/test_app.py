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
