from src.domain.user.model import User
from src.db import Session
from uuid_extensions import uuid7


def cretate_test_user():

    session = Session()
    user = User(name='test_user', email='a@test.com', id=uuid7())
    session.add(
        user
    )
    session.commit()
    id = user.id
    return id
