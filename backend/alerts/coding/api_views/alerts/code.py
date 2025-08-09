from ..decorator import require_jwt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ...services.alert.create import AlertCreateService
from ...services.alert.list import AlertListService
from ...services.alert.details import AlertDetailService
from ...services.alert.update import AlertUpdateService
from ...services.alert.delete import AlertDeleteService


@api_view(["POST", ])
@require_jwt
def create_api(request):
    call_response = AlertCreateService(request).execute()
    response_status, response_message, response_data = call_response[0], call_response[1], call_response[2]
    re_send = {
        'details': response_message,
        'data': response_data,
    }
    return Response(re_send, response_status)


@api_view(["GET", ])
@require_jwt
def list_api(request):
    call_response = AlertListService(request).execute()
    response_status, response_message, response_data = call_response[0], call_response[1], call_response[2]
    re_send = {
        'details': response_message,
        'data': response_data,
    }
    return Response(re_send, response_status)


@api_view(["GET", ])
@require_jwt
def details_api(request):
    call_response = AlertDetailService(request).execute()
    response_status, response_message, response_data = call_response[0], call_response[1], call_response[2]
    re_send = {
        'details': response_message,
        'data': response_data,
    }
    return Response(re_send, response_status)


@api_view(["PUT", ])
@require_jwt
def update_api(request):
    call_response = AlertUpdateService(request).execute()
    response_status, response_message, response_data = call_response[0], call_response[1], call_response[2]
    re_send = {
        'details': response_message,
        'data': response_data,
    }
    return Response(re_send, response_status)


@api_view(["DELETE", ])
@require_jwt
def delete_api(request):
    call_response = AlertDeleteService(request).execute()
    response_status, response_message, response_data = call_response[0], call_response[1], call_response[2]
    re_send = {
        'details': response_message,
        'data': response_data,
    }
    return Response(re_send, response_status)