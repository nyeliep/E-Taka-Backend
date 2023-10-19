from django.test import TestCase
from .models import Delivery
import datetime

class DeliveryTestCase(TestCase):
    def test_default_delivery_method(self):
        delivery = Delivery()
        self.assertEqual(delivery.delivery_method, 'Pickup')

    def test_default_delivery_status(self):
        delivery = Delivery()
        self.assertEqual(delivery.status, 'pending')

    def test_delivery_address_max_length(self):
        delivery = Delivery()
        max_length = delivery._meta.get_field('delivery_address').max_length
        self.assertEqual(max_length, 200)

    def test_default_delivery_address(self):
        delivery = Delivery()
        self.assertEqual(delivery.delivery_address, 'Address')
















