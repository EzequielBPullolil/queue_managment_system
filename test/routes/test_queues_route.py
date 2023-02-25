from flask import json


class TestQueueRoutes:
    def test_post_request(self, client):
        response = client.post('/queues',
                               json={
                                   "name": "test_queue"
                               },
                               content_type='application/json')

        assert response.status_code == 201
        data = json.loads(response.get_data(as_text=True))

        assert data['status'] == 'queue created'
        assert data['queue_id'] != None
