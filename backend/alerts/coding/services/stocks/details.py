from ....models import Stock
from ..base_validator import BaseValidator
class StockValidator(BaseValidator):
    def validate(self):
        try:
            stock = Stock.objects.get(symbol=self.value)
            self.response_status = 200
            self.response_data = {
                "symbol": stock.symbol,
                "name": stock.name,
                "price": stock.price,
            }
        except Stock.DoesNotExist:
            self.response_status = 404
            self.response_message = "Stock not found"

class StockDetailService:
    def __init__(self, request):
        self.request = request
    def execute(self):
        symbol = self.request.GET.get("symbol", "")
        details = StockValidator(symbol)
        details.validate()
        response_status, response_message, response_data = details.get_response()
        return response_status, response_message, response_data