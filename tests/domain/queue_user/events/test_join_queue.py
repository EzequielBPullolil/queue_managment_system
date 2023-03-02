from tests.utils.create_user import cretate_test_user


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
        assert received[0]['name'] == 'increment_queue_length'
        assert received[0]['args'][0] == queue_suject_id

    def test_join_queue_increment_user_ticket(self, sio, queue_suject_id):
        '''
            We verify that usert_ticket
            increases as users enter the queue
        '''
        sio.connect()
        assert sio.is_connected() == True

        # creates two user sujects
        user_one_id = cretate_test_user()
        user_two_id = cretate_test_user()

        sio.emit('join_queue', {
            'user_id': user_one_id,
            'queue_id': queue_suject_id
        })
        sio.emit('join_queue', {
            'user_id': user_two_id,
            'queue_id': queue_suject_id
        })

        received = sio.get_received()

        print(received)
        assert received[1]['name'] == 'user_ticket'
        user_one_ticket = received[1]['args'][0]
        assert received[3]['name'] == 'user_ticket'
        user_two_ticket = received[3]['args'][0]

        assert user_one_ticket < user_two_ticket
