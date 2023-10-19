from django.db import models
from django.contrib.auth.models import User
from useraccount.models import UserAccount

class Meta:
    app_label = 'order'

class Order(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    ORDER_STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('pending', 'Pending'),
    ]

    order_status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS_CHOICES,
        default='pending',
    )

    def __str__(self):
        return f"Order {self.pk} by {self.user.username} on {self.order_date}"

    class Meta:
        ordering = ["-order_date"]

