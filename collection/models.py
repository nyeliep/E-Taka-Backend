from django.db import models
from useraccount.models import UserAccount


EWASTE_TYPE_CHOICES = [
    ('Home Appliances', 'Home Appliances'),
    ('Phones', 'Phones'),
    ('Office Appliances', 'Office Appliances'),
    ('Gaming Gadgets', 'Gaming Gadgets'),
    ('Automotive Gadgets', 'Automotive Gadgets'),
]

STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Processing', 'Processing'),
    ('Completed', 'Completed'),
]

PAYMENT_STATUS_CHOICES = [
    ('Unpaid', 'Unpaid'),
    ('Paid', 'Paid'),
]

class EwasteRequest(models.Model):
    ewaste_type = models.CharField(max_length=50, choices=EWASTE_TYPE_CHOICES)
    quantity = models.PositiveIntegerField()
    pickup_date = models.DateField()
    is_collected = models.BooleanField(default=False)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='ewaste_images/')
    requester = models.ForeignKey(UserAccount, on_delete=models.CASCADE)


    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='Unpaid')



    def __str__(self):
        return f"Requester:{self.requester.username}"

