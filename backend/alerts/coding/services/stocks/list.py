from ....models import Stock
from extension.pagination import PaginatorService

class StockListService:
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
        stocks = Stock.objects.all()
        for stock in stocks:
            send_item = {
                "symbol": stock.symbol,
                "name": stock.name,
                "price": stock.price,
            }
            self.list_items.append(send_item)
        self.response_data = self.paginator.paginate_with_response(self.list_items, self.page)
        return self.response_status, self.response_message, self.response_data