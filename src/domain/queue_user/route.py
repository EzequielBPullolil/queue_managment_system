from flask import Blueprint, make_response
from sqlalchemy import select
from .model import Queue_User
from src.db import Session
queueUser_bp = Blueprint('queue_user', __name__, url_prefix='/queue_user')


@queueUser_bp.route('/<queue_id>',  methods=['GET'], strict_slashes=False)
def queued_users(queue_id):
    '''
        Response with every user queued in queue
    '''
    session = Session()

    response = session.execute(
        select(Queue_User).where(Queue_User.queue_id == queue_id)
    ).fetchall()[0]

    users = [i.as_dict() for i in response]
    response_data = {
        'status': 'queued_users',
        'users': users
    }
    return make_response(response_data, 200)
