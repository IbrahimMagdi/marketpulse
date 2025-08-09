from ..decorator import require_jwt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.alerts.coding.services.triggered.list import TriggeredAlertListService


@api_view(["GET"])
@require_jwt
def list_api(request):
    call_response = TriggeredAlertListService(request).execute()
    response_status, response_message, response_data = call_response[0], call_response[1], call_response[2]
    re_send = {
        'details': response_message,
        'data': response_data,
    }
    return Response(re_send, response_status)