from flask import json


class TestQueueUserRoute:
    def test_get_queued_users(self, client, queue_suject_id):
        '''
            Query queued user in queued with queue_id
        '''
        response = client.get(f'/queue_user/{queue_suject_id}')

        assert response.status_code == 200
