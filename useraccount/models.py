from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField



class UserAccount(AbstractUser):
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to="user_images/", null=True)
    location = models.CharField(max_length=32)
    phone_number = PhoneNumberField()
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128, null=False)

    def get_full_name(self):
        if self.first_name:
           return f"{self.first_name}"
        return self.username


    groups = models.ManyToManyField(
        'auth.Group',
        related_name='useraccount_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='useraccount_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )










