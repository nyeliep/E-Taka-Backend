from django.urls import path
from . import views

urlpatterns = [
    path('b2c_payment/', views.b2c_payment_view, name='b2c_payment'),
]
