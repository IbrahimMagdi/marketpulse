from ...base_validator import MessageHelper
from .user_name import UserNameAuthenticator
from .password_validator import PasswordAuthenticator
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


class SignInService:
    def __init__(self, request):
        self.request = request
        self.ln = request.META.get("HTTP_LN", "en")
        self.msg_helper = MessageHelper(request, "authentication")
        self.ty = request.headers.get('ty') or None
        self.tk = request.headers.get('tk') or None

    def execute(self):
        user_name = UserNameAuthenticator(self.request, self.request.POST.get("username", "").strip(), self.msg_helper)
        user_name.check_user()
        st, msg, data = user_name.get_response()
        if st != 200:
            return st, msg, None
        password = PasswordAuthenticator(self.request, self.request.POST.get("password", ""), self.msg_helper)
        st, msg, _ = password.authenticate_user(data)
        if st != 200:
            return st, msg, None
        refresh = RefreshToken.for_user(data)

        response_status = status.HTTP_200_OK
        response_data = {
            "session": {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            "info": {
                "id": str(data.id),
                "name": data.first_name,

            },
        }
        return response_status, "", response_data