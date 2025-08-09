from ....models import Alert
from ..base import *

class AlertValidator(BaseValidator):
    def __init__(self, user, value, msg_helper):
        super().__init__(value, msg_helper.lang)
        self.user = user
        self.alert_id = value
        self.msg_helper = msg_helper

    def validate(self):
        try:
            alert = Alert.objects.get(id=int(self.alert_id), user=self.user)
            self.response_status = 200
            self.response_data = {
                "stock": alert.stock.symbol,
                "alert_type": alert.alert_type,
                "condition": alert.condition,
                "threshold": alert.threshold,
                "duration": alert.duration,
                "is_active": alert.is_active,
            }
        except Alert.DoesNotExist:
            self.response_status = 404
            self.response_message = self.msg_helper.get("not_found")


class AlertDetailService:
    def __init__(self, request):
        self.request = request
        self.msg_helper = MessageHelper(request, "Alert")

    def execute(self):
        alert_id = self.request.GET.get("alert_id")
        if not alert_id or not alert_id.isdigit():
            return 400, "Invalid alert_id", None
        details = AlertValidator(self.request.user, alert_id, self.msg_helper)
        details.validate()
        response_status, response_message, response_data = details.get_response()
        return response_status, response_message, response_data