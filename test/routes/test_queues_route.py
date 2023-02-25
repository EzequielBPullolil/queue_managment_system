class TestQueueRoutes:
    def test_post_request(self, client):
        response = client.post('/queues', data={
            "name": "test_queue"
        })

        assert response.status_code == 201
        assert response.body['status'] == 'queue created'
        assert response.body['queue_id'] != None
