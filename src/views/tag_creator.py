from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.controller.tag_creator_controller import TagCreatorController
class TagCreator:
    
    def create_tag(self, http_request: HttpRequest) -> HttpResponse:
        tag_creator_controller = TagCreatorController()
        
        body = http_request.body
        
        product_code = body["product_code"]
        
        formatted_response = tag_creator_controller.create(product_code)
        
        return HttpResponse(status_code=200, body=formatted_response)