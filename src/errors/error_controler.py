from .http_bad_request import HttpBadRequestError
from .http_unprocessable_entity import HttpUnprocessableEntityError
from typing import Dict

def handle_error(error: Exception) -> Dict:
    if isinstance(error, (HttpBadRequestError, HttpUnprocessableEntityError)):
        return {
            "status_code": error.status_code,
            "body": {
                "errors": [
                    {
                        "title": error.name,
                        "message": error.message,
                    }
                ]
            },
        }
    else:
        return {
            "status_code": 500,
            "body": {
                "errors": [{"title": "Internal Server Error", "message": str(error)}],
            },
        }
