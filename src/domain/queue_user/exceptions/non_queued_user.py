class NonQueuedUser(Exception):
    def __init__(self, queue_id, user_id, *args: object) -> None:
        super().__init__(*args)
        self.message = f'User with id {user_id} not queued in queue by id {queue_id}'
