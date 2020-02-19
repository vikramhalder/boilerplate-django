from rest_framework.decorators import api_view

from api.view import apiresponse


@api_view(['GET'])
def index(request):
    return apiresponse.response(True, None, "success")
