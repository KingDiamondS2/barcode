from flask import Blueprint, request, jsonify

from src.errors.error_handler import handle_errors
from src.validators.tag_creator_validator import tag_creator_validator

from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator import TagCreator

route_bp = Blueprint('route', __name__)

@route_bp.route('/create_tag', methods=["POST"])
def create_tag():
    response = None
    try:
        tag_creator_validator(request)
        tag_creator = TagCreator()
        
        http_request = HttpRequest(body= request.json)
        
        response = tag_creator.create_tag(http_request)
    except Exception as exception:
        response=handle_errors(exception)
    
    return jsonify(response.body), response.status_code