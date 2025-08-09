from ....models import Alert

class AlertDeleteService:
    def __init__(self, request):
        self.request = request
        self.response_status = 400
        self.response_message = ""
        self.response_data = None
        self.alert_id = self.request.POST.get("alert_id")

    def execute(self):
        if not self.alert_id or not self.alert_id.isdigit():
            self.response_message = "Invalid alert_id"
        try:
            alert = Alert.objects.get(id=self.alert_id, user=self.request.user)
            alert.delete()
            self.response_status = 202
            self.response_message = "Alert deleted successfully"
        except Alert.DoesNotExist:
            self.response_status = 404
            self.response_message = "Alert not found"
        return self.response_status, self.response_message, self.response_data