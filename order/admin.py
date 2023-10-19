from django.contrib import admin
from order.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "quantity",
        "total_price",
        "order_date",
        "order_status",
    )


    list_filter = ("order_status", "order_date")


admin.site.register(Order, OrderAdmin)
