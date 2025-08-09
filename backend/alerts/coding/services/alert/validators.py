from backend.alerts.models import Stock
from backend.alerts.coding.services.base import BaseValidator
from datetime import timedelta

class AlertValidator(BaseValidator):
    def __init__(self, data, msg_helper):
        super().__init__(data, msg_helper.lang)
        self.msg_helper = msg_helper
        self.data = data
        self.response_data = {}

    def validate(self):
        # --- 1. Validate stock symbol ---
        symbol = self.data.get("stock", "").strip().upper()
        if not symbol:
            self.response_status = 400
            self.response_message = self.msg_helper.get("check_stock", "none")
            return
        try:
            stock = Stock.objects.get(symbol=symbol)
        except Stock.DoesNotExist:
            self.response_status = 400
            self.response_message = self.msg_helper.get("check_stock", "not_found")
            return

        # --- 2. Validate alert_type ---
        alert_type = self.data.get("alert_type")
        if alert_type not in ("PRICE", "DURATION"):
            self.response_status = 400
            self.response_message = self.msg_helper.get("check_type", "invalid")
            return

        # --- 3. Validate condition ---
        condition = self.data.get("condition")
        if condition not in ("ABOVE", "BELOW"):
            self.response_status = 400
            self.response_message = self.msg_helper.get("check_condition", "invalid")
            return

        # --- 4. Validate threshold ---
        try:
            threshold = float(self.data.get("threshold"))
        except (TypeError, ValueError):
            self.response_status = 400
            self.response_message = self.msg_helper.get("check_threshold", "invalid")
            return

        # --- 5. Validate duration (if duration alert) ---
        duration = None
        if alert_type == "DURATION":
            dur = self.data.get("duration")
            try:
                duration = int(dur)
                if duration < 1:
                    raise ValueError
                duration = timedelta(hours=duration)
            except (TypeError, ValueError):
                self.response_status = 400
                self.response_message = self.msg_helper.get("check_duration", "invalid")
                return

        # --- Success! ---
        self.response_status = 200
        self.response_data = {
            "stock": stock,
            "alert_type": alert_type,
            "condition": condition,
            "threshold": threshold,
            "duration": duration,
        }