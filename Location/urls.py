from django.urls import path
from .views import get_location_coordinates



urlpatterns = [
     path('getlocation/', get_location_coordinates, name='process_location_views'),
]