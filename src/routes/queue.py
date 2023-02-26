from flask import Blueprint, jsonify, request, make_response
from src.db import Session
from src.db.models import Queue
from uuid_extensions import uuid7
queue_bp = Blueprint('queues', __name__, url_prefix='/queues')


@queue_bp.route('/',  methods=['POST'], strict_slashes=False)
def create_queue():
    '''
        Create queue and response
        with queue id
    '''
    response_data = {}
    sesion = Session()
    json_data = request.get_json()
    name = json_data['name']
    queue = Queue(id=uuid7(), name=name)

    sesion.add(queue)
    sesion.commit()

    response_data['status'] = 'queue created'
    response_data['queue_id'] = queue.id
    return make_response(response_data, 201)
