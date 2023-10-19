from django.db import models
from Cart.models import Cart

class Product(models.Model):

    TELEVISION = 'television'
    FRIDGES = 'fridges'
    PHONES = 'phones'
    CABLES = 'cables'
    WOOFERS = 'woofers'
    RADIO = 'radio'
    LAPTOPS = 'laptops'
    MICROWAVE = 'microwave'

    CATEGORY_CHOICES = [
        (TELEVISION, 'Television'),
        (FRIDGES, 'Fridges'),
        (PHONES, 'Phones'),
        (CABLES, 'Cables'),
        (WOOFERS, 'Woofers'),
        (RADIO, 'Radio'),
        (LAPTOPS, 'Laptops'),
        (MICROWAVE, 'Microwave'),
    ]
    product_name=models.CharField(max_length=32, null=True)
    price =models.DecimalField(max_digits=8,decimal_places=2)
    description = models.TextField(max_length=255)
    image =models.ImageField(upload_to='images')
    is_available=models.BooleanField(default=False)
    quantity_of_items=models.PositiveIntegerField(default=0)
    product_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    cart = models.ManyToManyField(Cart,null=True ,related_name='products')
