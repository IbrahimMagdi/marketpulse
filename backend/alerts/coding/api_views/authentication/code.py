from rest_framework.response import Response
from rest_framework.decorators import api_view
from ...services.authentication.sign_up.create import SignUpService
from ...services.authentication.sign_in.view import SignInService


@api_view(["POST", ])
def signup_api(request):
    call_response = SignUpService(request).execute()
    response_status, response_message, response_data = call_response[0], call_response[1], call_response[2]
    re_send = {
        'details': response_message,
        'data': response_data,
    }
    return Response(re_send, response_status)

@api_view(["POST", ])
def signin_api(request):
    call_response = SignInService(request).execute()
    response_status, response_message, response_data = call_response[0], call_response[1], call_response[2]
    re_send = {
        'details': response_message,
        'data': response_data,
    }
    return Response(re_send, response_status)