from django.contrib import admin
from .models import Delivery


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('customer_name','delivery_address','delivery_time','delivery_method','status','order')
admin.site.register(Delivery, DeliveryAdmin)