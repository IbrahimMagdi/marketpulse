from ..sign_up.base_validator import BaseValidator
from  extension.string import Extension
from .....models import User

class UserNameValidator(BaseValidator):
    def __init__(self, request, value, msg_helper):
        super().__init__(value, msg_helper.lang)
        self.msg_helper = msg_helper
        self.request = request

    def validate(self):
        ext_email = Extension(self.value or "")
        checks = [
            ext_email.validate_required(self.msg_helper.get("SignUp", "check_email", "none")),
            ext_email.validate_email_format(self.msg_helper.get("SignUp", "check_email", "incorrect")),
        ]

        for ok, msg in checks:
            if not ok:
                self.response_message = msg
                return
        self.response_status = 200

class UserNameAuthenticator(UserNameValidator):
    def check_user(self):
        self.validate()
        st, msg, data = self.get_response()
        if st != 200:
            return st, msg, None
        try:
            user = User.objects.get(email=self.value)
            self.response_data = user
        except User.DoesNotExist:
            self.response_status = 400
            self.response_message = self.msg_helper.get("SignIn", "check_password", "incorrect")
            self.response_data = None
        return self.response_status, self.response_message, self.response_data


