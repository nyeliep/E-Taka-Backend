from django.test import TestCase
from product.models import Product


class ProductModelTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            product_name="Test Product",
            price=100.00,
            description="Test description",
            image="test.jpg",
            is_available=True
            quantity_of_items=10,
            category=Product.TELEVISION)



    def test_product_creation(self):
        self.assertEqual(str(self.product.product_name), "Test Product")
        self.assertEqual(self.product.description, "Test description")
        self.assertEqual(self.product.image, "test.jpg")
        self.assertTrue(self.product.is_available)
        self.assertEqual(self.product.quantity_of_items, 10)
        self.assertEqual(self.product.category, Product.TELEVISION)

    def test_category_choices(self):
        choices = [choice[0] for choice in Product.CATEGORY_CHOICES]
        self.assertIn(Product.TELEVISION, choices)
        self.assertIn(Product.FRIDGES, choices)
        self.assertIn(Product.PHONES, choices)
        self.assertIn(Product.CABLES, choices)
        self.assertIn(Product.WOOFERS, choices)
        self.assertIn(Product.RADIO, choices)
        self.assertIn(Product.LAPTOPS, choices)
        self.assertIn(Product.MICROWAVE, choices)



    def test_default_availability(self):
        default_product = Product.objects.create(
            product_name="Default Product",
            price=50.00,
            description="Default description",
            image="default.jpg",
            quantity_of_items=5,
            category=Product.PHONES
        )
        self.assertFalse(default_product.is_available)
