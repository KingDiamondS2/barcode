from src.views.http_types.http_response import HttpResponse
from src.errors.error_types.http_unprocessable import HttpUnprocessable

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessable):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors":[{
                    "title": error.name,
                    "details": error.message
                }]
            }
        )
    
    return HttpResponse(
        status_code=500,
        body={
            "errors":[{
                "title": "server error",
                "details": str(error)
            }]
        }
    )