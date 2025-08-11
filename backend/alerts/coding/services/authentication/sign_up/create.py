from ...base_validator import *
from .name_validator import NameValidator
from .email_validator import EmailValidator
from .password_validator import PasswordValidator
from .....models import *
from rest_framework import status
import secrets, string
from rest_framework_simplejwt.tokens import RefreshToken


class SignUpService:
    def __init__(self, request):
        self.request = request
        self.ln = request.META.get("HTTP_LN", "en")
        self.msg_helper = MessageHelper(request, "authentication")
        self.name = self.email = self.password = None



    def validate_all(self):
        name_val = NameValidator(self.request.POST.get("name", "").strip(), self.msg_helper)
        name_val.validate()
        st, msg, _ = name_val.get_response()
        if st != 200:
            return st, msg
        self.name = name_val.value

        email_val = EmailValidator(self.request.POST.get("email", "").strip(), self.msg_helper)
        email_val.validate()
        st, msg, _ = email_val.get_response()
        if st != 200:
            return st, msg
        self.email = email_val.value

        pass_val = PasswordValidator(self.request.POST.get("password", ""), self.msg_helper)
        pass_val.validate()
        st, msg, _ = pass_val.get_response()
        if st != 200:
            return st, msg
        self.password = pass_val.value

        return 200, ""

    @staticmethod
    def generate_username():
        characters = string.ascii_lowercase + string.digits
        for _ in range(20):
            candidate = ''.join(secrets.choice(characters) for _ in range(16))
            if not User.objects.filter(username=candidate).exists():
                return candidate
        raise Exception("Failed to generate unique username")

    def create_user_account(self):
        return User.objects.create_user(
            username=self.generate_username(),
            first_name=self.name,
            email=self.email,
            password=self.password,
        )

    def execute(self):
        st, msg = self.validate_all()
        if st != 200:
            return st, msg, None
        user = self.create_user_account()
        response_status = status.HTTP_201_CREATED
        refresh = RefreshToken.for_user(user)

        response_data = {
            "session": {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },

        }
        return response_status, "", response_data


