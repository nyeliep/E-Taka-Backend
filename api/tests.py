from django.test import TestCase ,Client
from Cart.models import Cart  

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from product.models import Product

from django.contrib.auth.models import User
from order.models import Order
# from api.serializer import OrderSerializer





class ProductAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.product_data = {
            "product_name": "Test Product",
            "price": "100.00",
            "description": "Test description",
            "image": "test.jpg",
            "is_available": True,
            "quantity_of_items": 10,
            "category": Product.TELEVISION,
        }
        self.product = Product.objects.create(**self.product_data)
        self.api_url = reverse("product_list_view") 

    def test_get_product_list(self):
        response = self.client.get(self.api_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        response = self.client.post(self.api_url, self.product_data, format="json")
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
class CartAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.cart_data = {
        }
        self.cart = Cart.objects.create(**self.cart_data)
        self.cart_url = reverse("cart-list") 






class OrderListViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.force_authenticate(user=self.user)
        self.order_data = {
            'user': self.user.id,
            'quantity': 5,
            'total_price': '50.00',
            'order_status': 'pending'
        }

    def test_create_order(self):
        url = reverse('order_list')
        response = self.client.post(url, self.order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_orders(self):
        url = reverse('order_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class OrderDetailViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.force_authenticate(user=self.user)
        self.order = Order.objects.create(
            user=self.user,
            quantity=5,
            total_price='50.00',
            order_status='pending'
        )

    def test_retrieve_order(self):
        url = reverse('order_detail', args=[self.order.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_order(self):
        url = reverse('order_detail', args=[self.order.id])
        updated_data = {
            'user': self.user.id,
            'quantity': 3,
            'total_price': '30.00',
            'order_status': 'confirmed'
        }
        response= self.client.put(url,updated_data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_order(self):
        url = reverse('order_detail', args=[self.order.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


