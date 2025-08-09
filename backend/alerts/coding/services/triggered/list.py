from ....models import TriggeredAlert
from extension.pagination import PaginatorService

class TriggeredAlertListService:
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
        triggered_alerts = TriggeredAlert.objects.filter(alert__user=self.request.user)
        for triggered_alert in triggered_alerts:
            send_item = {
                "id": triggered_alert.id,
                "alert_id": triggered_alert.alert.id,
                "stock": triggered_alert.alert.stock.symbol,
                "price": triggered_alert.price,
                "details": triggered_alert.details,
            }
            self.list_items.append(send_item)
        self.response_data = self.paginator.paginate_with_response(self.list_items, self.page)
        return self.response_status, self.response_message, self.response_data


