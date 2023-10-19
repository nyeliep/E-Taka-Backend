from django.db import models
from datetime import timedelta
from django.conf import settings
import datetime
from django.utils import timezone
from order.models import Order

class Meta:
    app_label = 'delivery'


DELIVERY_TIME_OPTIONS = (
    ('mins', 'Minutes'),
    ('hrs', 'Hours')
    )

DELIVERY_CHOICES = [
        ('pickup' , 'Pickup'),
        ('home delivery' , 'Home Delivery')
    ]

DELIVERY_STATUS= [
    ('pending' , 'Pending'),
    ('on-going' , 'On-going'),
    ('delivered' , 'Delivered')

]
class Delivery(models.Model):
    order = models.ForeignKey( Order, on_delete=models.CASCADE, related_name='delivery')

    customer_name = models.CharField(max_length = 100, default = 'customer')
    delivery_address = models.CharField(max_length=200, default='Address')
    delivery_time = models.DateTimeField(default = timezone.now)
    delivery_method = models.CharField( max_length=20 ,choices= DELIVERY_CHOICES, default='Pickup')   
    status = models.CharField(max_length=26, choices= DELIVERY_STATUS, default = 'pending')


    def get_delivery_time_timedelta(self):
        if self.delivery_unit == 'hrs':
            return timedelta(hours=self.delivery_time.hour)
        else:
            return timedelta(minutes=self.delivery_time.minute)

    class Meta:
         verbose_name = 'Delivery'
         verbose_name_plural = 'Deliveries'
         db_table = 'Delivery'

    

    