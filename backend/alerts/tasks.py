import os
import requests
from django.utils import timezone
from celery import shared_task
from .models import Stock, Alert, TriggeredAlert
from django.core.mail import send_mail
from django.conf import settings

STOCK_SYMBOLS = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'NFLX', 'NVDA', 'PYPL', 'ADBE']


@shared_task
def fetch_stock_prices():
    api_key = os.getenv('STOCK_API_KEY', 'demo')
    for symbol in STOCK_SYMBOLS:
        try:
            url = f"https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={api_key}"
            response = requests.get(url)
            data = response.json()

            if data and isinstance(data, list) and len(data) > 0:
                stock_data = data[0]
                stock, created = Stock.objects.update_or_create(
                    symbol=symbol,
                    defaults={
                        'name': stock_data.get('name', ''),
                        'price': stock_data.get('price')
                    }
                )
        except Exception as e:
            print(f"Error fetching {symbol}: {str(e)}")

@shared_task
def check_alerts():
    active_alerts = Alert.objects.filter(is_active=True)
    for alert in active_alerts:
        try:
            if alert.alert_type == 'PRICE':
                check_price_alert(alert)
            elif alert.alert_type == 'DURATION':
                check_duration_alert(alert)
        except Exception as e:
            print(f"Error checking alert {alert.id}: {str(e)}")

def check_price_alert(alert):
    current_price = alert.stock.price
    if alert.condition == 'ABOVE' and current_price > alert.threshold:
        trigger_alert(alert, current_price, f"Price reached {current_price}, above threshold {alert.threshold}")
    elif alert.condition == 'BELOW' and current_price < alert.threshold:
        trigger_alert(alert, current_price, f"Price reached {current_price}, below threshold {alert.threshold}")

def check_duration_alert(alert):
    current_price = alert.stock.price
    now = timezone.now()
    condition_met = (
            (alert.condition == 'ABOVE' and current_price > alert.threshold) or
            (alert.condition == 'BELOW' and current_price < alert.threshold)
    )

    if condition_met:
        if not alert.condition_met_since:
            alert.condition_met_since = now
            alert.save()
        else:
            duration_met = now - alert.condition_met_since
            if duration_met >= alert.duration:
                trigger_alert(
                    alert,
                    current_price,
                    f"Price stayed {alert.condition.lower()} {alert.threshold} for {duration_met}"
                )
                alert.condition_met_since = None
                alert.save()
    else:
        if alert.condition_met_since:
            alert.condition_met_since = None
            alert.save()

def trigger_alert(alert, price, details):
    TriggeredAlert.objects.create(
        alert=alert,
        price=price,
        details=details
    )
    alert.triggered_count += 1
    alert.save()
    send_alert_notification(alert, price, details)

def send_alert_notification(alert, price, details):
    subject = f"Stock Alert: {alert.stock.symbol} {alert.get_condition_display()} {alert.threshold}"
    message = (
        f"Hello {alert.user.first_name},\n\n"
        f"Your stock alert for {alert.stock.symbol} ({alert.stock.name}) has been triggered.\n"
        f"Current price: ${price:.2f}\n"
        f"Alert condition: {details}\n\n"
        "You can manage your alerts at our platform.\n\n"
        "Best regards,\nStock Alert Team"
    )
    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [alert.user.email],
            fail_silently=False,
        )
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
    print(f"Alert triggered: {subject}")