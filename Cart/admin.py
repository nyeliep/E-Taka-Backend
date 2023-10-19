
from django.contrib import admin
from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ["created_at","updated_at","total_items","total_price"] 
admin.site.register(Cart)




