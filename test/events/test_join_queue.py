class TestJoinQueue:
    queue_length = 0

    def test_join_queue_increment_queue_length(self, sio):
        '''
            verify if join_queue call
            increment queue_length
        '''
        for i in range(self.queue_length, 10):
            '''
                Run 10 times the event join_queue and verify if
                queue_length increment
            '''
            sio.connect()
            assert sio.is_connected() == True
            sio.emit('join_queue')
            received = sio.get_received()
            queue_status = received[0]
            queue_data = queue_status['args'][0]
            sio.disconnect()
            self.queue_length = queue_data['queue_length']

        assert self.queue_length == 10
