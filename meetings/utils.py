from rest_framework.response import Response


def create_response(data):
    response_dto = {
        "statusCode": 0,
        "isSuccess": True,
        "message": "Success operation",
        "data": data,
    }
    return Response(response_dto)
