from django.contrib import admin
from .models import EwasteRequest

class EwasteRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'ewaste_type', 'quantity', 'pickup_date', 'location', 'status', 'payment_status', 'requester')
    list_filter = ('ewaste_type', 'status', 'payment_status')
    search_fields = ('location', 'requester__username')  # Example fields to search by
    date_hierarchy = 'pickup_date'

admin.site.register(EwasteRequest, EwasteRequestAdmin)

