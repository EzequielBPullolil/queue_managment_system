class TestJoinQueue:
    def test_leave_queue_reduce_queue_length(self, sio):
        '''
            Count queue length and emits leave_queue event
            and compare if queue_length are lower 
        '''
        pre_leave_queue_length = None
        sio.connect()

        assert sio.is_connected() == True
        sio.emit('join_queue')
        received = sio.get_received()
        queue_status = received[0]
        queue_data = queue_status['args'][0]

        pre_leave_queue_length = queue_data['queue_length']

        sio.emit('leave_queue')

        received = sio.get_received()

        queue_status = received[0]
        queue_data = queue_status['args'][0]
        assert pre_leave_queue_length > queue_data['queue_length']
