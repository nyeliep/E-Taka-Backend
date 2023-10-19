from django.db import models

class Payment(models.Model):
    user_phone_number = models.CharField(max_length=14)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment ID: {self.id}, Transaction ID: {self.transaction_id}"

