from ..decorator import require_jwt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.alerts.coding.services.stocks.list import StockListService
from backend.alerts.coding.services.stocks.details import StockDetailService


@api_view(["GET"])
@require_jwt
def list_api(request):
    call_response = StockListService(request).execute()
    response_status, response_message, response_data = call_response[0], call_response[1], call_response[2]
    re_send = {
        'details': response_message,
        'data': response_data,
    }
    return Response(re_send, response_status)

@api_view(["GET"])
@require_jwt
def details_api(request):
    call_response = StockDetailService(request).execute()
    response_status, response_message, response_data = call_response[0], call_response[1], call_response[2]
    re_send = {
        'details': response_message,
        'data': response_data,
    }
    return Response(re_send, response_status)