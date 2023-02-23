class TestJoinQueue:
    queue_length = 0

    def test_join_queue_increment_queue_length(self, sio):
        '''
            verify if join_queue call
            increment queue_length
        '''
        print('test: Join queue increment-----------------------------')
        for i in range(0, 10):
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

    def test_join_queue_not_return_the_same_ticket(self, sio):
        '''
            Verify if queue_status not send the same 
            [actual_ticket]
        '''
        print('test: Join queeu ticket-----------------------------')

        last_ticket = None
        for i in range(0, 10):
            sio.connect()
            assert sio.is_connected() == True
            sio.emit('join_queue')
            received = sio.get_received()
            queue_status = received[0]
            queue_data = queue_status['args'][0]
            sio.disconnect()
            assert queue_data['actual_ticket'] != last_ticket
            last_ticket = queue_data['actual_ticket']
