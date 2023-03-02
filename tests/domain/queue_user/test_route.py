from flask import json


class TestQueueUserRoute:
    def test_get_queued_users(self, client, queue_suject_id):
        '''
            Query queued user in queued with queue_id
        '''
        response = client.get(f'/queues_user/{queue_suject_id}')

        assert response.status_code == 200
        data = json.loads(response.get_data(as_text=True))

        assert data['status'] == 'queue created'
        assert data['queue_id'] != None
