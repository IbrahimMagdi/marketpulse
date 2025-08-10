from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Stock(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    price = models.FloatField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.symbol} - {self.name}"


class Alert(models.Model):
    ALERT_TYPES = [
        ('PRICE', 'Price Threshold'),
        ('DURATION', 'Duration Alert'),
    ]

    CONDITIONS = [
        ('ABOVE', 'Above'),
        ('BELOW', 'Below'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    alert_type = models.CharField(max_length=10, choices=ALERT_TYPES)
    condition = models.CharField(max_length=10, choices=CONDITIONS, blank=True, null=True)
    threshold = models.FloatField()
    duration = models.DurationField(blank=True, null=True)  # For duration alerts
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    triggered_count = models.IntegerField(default=0)

    # For duration alerts tracking
    condition_met_since = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} - {self.stock.symbol}"


class TriggeredAlert(models.Model):
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE)
    triggered_at = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    details = models.TextField()

    def __str__(self):
        return f"{self.alert} triggered at {self.triggered_at}"