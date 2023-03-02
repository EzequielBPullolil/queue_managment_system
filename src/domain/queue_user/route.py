from flask import Blueprint, make_response

queueUser_bp = Blueprint('queue_user', __name__, url_prefix='/queue_user')


@queueUser_bp.route('/<queue_id>',  methods=['GET'], strict_slashes=False)
def queued_users(queue_id):
    '''
        Response with every user queued in queue 
    '''
    response_data = {}
    return make_response(response_data, 200)
