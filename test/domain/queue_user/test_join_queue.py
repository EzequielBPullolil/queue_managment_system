class TestJoinQueue:
    def test_join_queue_emits_increment_queue_length_event(self, sio, queue_suject_id, user_suject_id):
        '''
            verify if join_queue call
            increment queue_length
        '''

        # Sio join_queue event emit
        sio.connect()
        assert sio.is_connected() == True
        sio.emit('join_queue', {
            'queue_id': queue_suject_id,
            'user_id': user_suject_id
        })

        received = sio.get_received()
        print(received)

        assert len(received) > 0
        assert received[0]['name'] == 'increase_queue_length'
        assert received[0]['args'][0] == queue_suject_id
