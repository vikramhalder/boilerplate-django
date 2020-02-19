from rest_framework.response import Response


def response(status, data, message):
    return Response({
        "status": status,
        "message": message,
        "data": data
    });
