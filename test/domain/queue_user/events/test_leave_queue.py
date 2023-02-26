class TestLeaveQueue:
    def test_leave_queue_emit_decrement_queue_length(self, sio, queue_user):
        '''
            Verify if leave queue decrement queue_length 
        '''

        sio.connect()
        assert sio.is_connected() == True

        sio.emit('leave_queue', queue_user)

        received = sio.get_received()

        assert len(received) > 0

        assert received[0]['name'] == 'decrement_queue'
        assert received[0]['args'][0] == queue_user['queue_id']
