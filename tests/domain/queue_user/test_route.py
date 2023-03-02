from flask import json


class TestQueueUserRoute:
    def test_get_queued_users(self, client, queue_user):
        '''
            Query queued user in queued with queue_id
        '''
        response = client.get(f'/queue_user/{queue_user["queue_id"]}')

        assert response.status_code == 200
        data = json.loads(response.get_data())

        status = data['status']
        users = data['users']
        assert status == 'queued_users'
        assert type(users) == list

        assert len(users) > 0

        assert users[0]['user_id'] == queue_user['user_id']
