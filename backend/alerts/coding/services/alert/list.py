from ....models import Alert
from extension.pagination import PaginatorService

class AlertListService:
    def __init__(self, request):
        self.request = request
        self.list_items = []
        try:
            self.page = int(self.request.GET.get('page'))
        except:
            self.page = 1
        self.paginator = PaginatorService(per_page=10)
        self.response_status = 200
        self.response_message = ""
        self.response_data = {}

    def execute(self):
        alerts = Alert.objects.filter(user=self.request.user)
        for alert in alerts:
            send_item = {
                "id": alert.id,
                "stock": alert.stock.symbol,
                "alert_type": alert.alert_type,
                "condition": alert.condition,
                "threshold": alert.threshold,
                "duration": alert.duration,
                "is_active": alert.is_active,
            }
            self.list_items.append(send_item)
        self.response_data = self.paginator.paginate_with_response(self.list_items, self.page)
        return self.response_status, self.response_message, self.response_data
