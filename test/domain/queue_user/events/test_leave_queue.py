from pytest import raises
from src.domain.queue_user.exceptions import NonQueuedUser


class TestLeaveQueue:
    def test_event_emit_decrement_queue_length(self, sio, queue_user):
        '''
            Verify if leave queue decrement queue_length 
        '''

        sio.connect()
        assert sio.is_connected() == True

        sio.emit('leave_queue', queue_user)

        received = sio.get_received()

        assert len(received) > 0

        assert received[0]['name'] == 'decrement_queue_length'
        assert received[0]['args'][0] == queue_user['queue_id']

    def test_call_event_wiouth_begin_queued_throws_an_error(self, sio, user_suject_id, queue_suject_id):
        '''
            Verify if emits leave_queue wiouth stay queued 
            raise error 
        '''
        sio.connect()
        assert sio.is_connected() == True

        with raises(NonQueuedUser) as exception:
            sio.emit('leave_queue', {
                "user_id": user_suject_id,
                "queue_id": queue_suject_id
            })
            assert exception.type == NonQueuedUser

        received = sio.get_received()
