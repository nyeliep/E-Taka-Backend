from django.contrib import admin
from product.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=("product_name","price","description","image","quantity_of_items","category","is_available")
    pass

admin.site.register(Product,ProductAdmin)

