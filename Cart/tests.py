from django.test import TestCase

from .models import Cart



from django.test import TestCase
from .models import Product

class CartItemModelTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(product_name='Test Product', price=19.99)

    def test_cart_item_creation(self):
        cart_item = Cart.objects.create(
            product=self.product,
            quantity=2,
            price=19.99
        )

        self.assertEqual(cart_item.product, self.product)
        self.assertEqual(cart_item.quantity, 2)
        self.assertEqual(cart_item.price, 19.99)
