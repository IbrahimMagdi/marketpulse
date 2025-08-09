import json
from .validators import AlertValidator
from ....models import Alert
from ..base import MessageHelper
from datetime import timedelta
class AlertCreateService:
    def __init__(self, request):
        self.request = request
        self.user = request.user
        self.data = json.loads(request.body)
        self.ln = request.META.get("HTTP_LN", "en")
        self.msg_helper = MessageHelper(request, "Alert")

    def execute(self):
        alert_val = AlertValidator(self.data, self.msg_helper)
        alert_val.validate()
        st, msg, validated_data = alert_val.get_response()
        if st != 200:
            return st, msg, None

        alert = Alert.objects.create(
            user=self.user,
            stock=validated_data["stock"],
            alert_type=validated_data["alert_type"],
            condition=validated_data["condition"],
            threshold=validated_data["threshold"],
            duration=validated_data["duration"],
            is_active=True,
        )
        response_status = 201
        response_message = ""
        response_data = {
            "id": alert.id,
            "stock": alert.stock.symbol,
            "alert_type": alert.alert_type,
            "condition": alert.condition,
            "threshold": alert.threshold,
            "duration": alert.duration,
        }
        return response_status, response_message, response_data

