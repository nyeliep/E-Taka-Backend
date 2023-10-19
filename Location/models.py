
from django.db import models
import math
from math import radians, sin, cos, sqrt, atan2

class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

    def calculate_distance(self, other_location):
        R = 6371
        lat1 = math.radians(float(self.latitude))
        lon1 = math.radians(float(self.longitude))

        lat2 = math.radians(float(other_location.latitude))
        lon2 = math.radians(float(other_location.longitude))

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        distance = R * c

        return distance

# class User(models.Model):
#     username = models.CharField(max_length=100)
#     location = models.ForeignKey(Location, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.username
