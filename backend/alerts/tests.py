from django.test import TestCase
from django.contrib.auth.models import User
from .models import Stock, Alert
from datetime import timedelta

class AlertModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='ali',
            email='ali@test.com',
            password='password'
        )
        self.stock = Stock.objects.create(symbol='AAPL', name='Apple')

    def test_create_price_alert(self):
        alert = Alert.objects.create(
            user=self.user,
            stock=self.stock,
            alert_type='PRICE',
            condition='ABOVE',
            threshold=150
        )

        self.assertEqual(alert.user.username, 'ali')
        self.assertEqual(alert.stock.symbol, 'AAPL')
        self.assertEqual(alert.alert_type, 'PRICE')
        self.assertEqual(alert.condition, 'ABOVE')
        self.assertEqual(alert.threshold, 150)
        self.assertIsNone(alert.duration)
        self.assertTrue(alert.is_active)

    def test_create_duration_alert(self):
        alert = Alert.objects.create(
            user=self.user,
            stock=self.stock,
            alert_type='DURATION',
            condition='BELOW',
            threshold=120,
            duration=timedelta(hours=2)
        )

        self.assertEqual(alert.alert_type, 'DURATION')
        self.assertEqual(alert.condition, 'BELOW')
        self.assertEqual(alert.duration, timedelta(hours=2))

    def test_default_is_active(self):
        alert = Alert.objects.create(
            user=self.user,
            stock=self.stock,
            alert_type='PRICE',
            condition='ABOVE',
            threshold=200
        )
        self.assertTrue(alert.is_active, "is_active should be True by default")
