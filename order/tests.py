from django.test import TestCase
from django.contrib.auth.models import User
from decimal import Decimal
from order.models import Order

class OrderModelTestCase(TestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_create_order(self):
        order = Order.objects.create(
            user=self.user,
            quantity=5,
            total_price=Decimal('50.00'),
            order_status='pending'
        )
        self.assertEqual(order.quantity, 5)
        self.assertEqual(order.total_price, Decimal('50.00'))
        self.assertEqual(order.order_status, 'pending')
        self.assertEqual(order.user, self.user)

    def test_order_str(self):
        order = Order.objects.create(
            user=self.user,
            quantity=5,
            total_price=Decimal('50.00'),
            order_status='confirmed'
        )
        expected_str = f"Order {order.pk} by {self.user.username} on {order.order_date}"
        self.assertEqual(str(order), expected_str)

    def test_order_date_auto_now_add(self):
        order = Order.objects.create(
            user=self.user,
            quantity=5,
            total_price=Decimal('50.00'),
            order_status='confirmed'
        )
        self.assertIsNotNone(order.order_date)

    def test_order_default_status(self):
        order = Order.objects.create(
            user=self.user,
            quantity=5,
            total_price=Decimal('50.00')
        )
        self.assertEqual(order.order_status, 'pending')

def test_order_status_choices(self):
    with self.assertRaises(ValueError):

        Order.objects.create(
            user=self.user,
            quantity=5,
            total_price=Decimal('50.00'),
            order_status='invalid_status'
        )


    Order.objects.create(
        user=self.user,
        quantity=5,
        total_price=Decimal('50.00'),
        order_status='confirmed'
    )


