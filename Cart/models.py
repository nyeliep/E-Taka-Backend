
from django.db import models
from useraccount.models import UserAccount


class Cart(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def calculate_total(self):
        total = sum(item.product.price * item.quantity for item in self.items.all())
        return total





