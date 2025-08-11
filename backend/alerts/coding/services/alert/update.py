import json
from .validators import AlertValidator
from ....models import Alert
from ..base_validator import MessageHelper

class AlertUpdateService:
    def __init__(self, request):
        self.request = request
        self.user = request.user
        self.data = json.loads(request.body)
        self.ln = request.META.get("HTTP_LN", "en")
        self.msg_helper = MessageHelper(request, "Alert")
        self.alert_id = self.data.get("alert_id")

    def execute(self):
        try:
            alert = Alert.objects.get(id=self.alert_id, user=self.user)
        except Alert.DoesNotExist:
            response_status = 404
            response_message = self.msg_helper.get("not_found")
            return response_status, response_message, None
        alert_val = AlertValidator(self.data, self.msg_helper)
        alert_val.validate()
        response_status, response_message, validated_data = alert_val.get_response()
        if response_status != 200:
            return response_status, response_message, None
        for key, value in validated_data.items():
            setattr(alert, key, value)
        alert.save()

        response_status = 202
        response_message = ""
        response_data =  {
            "id": alert.id,
            "stock": alert.stock.symbol,
            "alert_type": alert.alert_type,
            "condition": alert.condition,
            "threshold": alert.threshold,
            "duration": alert.duration,
            "is_active": alert.is_active,
        }

        return response_status, response_message, response_data
