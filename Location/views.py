    

# from django.http import HttpResponse
import math
from math import radians, sin, cos, sqrt, atan2

def get_location_coordinates(request):
    if request.method == 'POST':

        # Getting latitude and longitude directly from the request
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        # Company's location
        lat1 = math.radians(float(-1.174425))
        lon1 = math.radians(float(36.753562))
        
        # Customer's location            
        lat2 = math.radians(float(latitude))
        lon2 = math.radians(float(longitude))

        # Calculate distance
        R = 6371 
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        distance = R * c 

    #     # Calculating shipping fee
    #     def calculate_shipping_fee(distance):
    #         fee_per_5_km = 100
    #         shipping_fee = (math.ceil(distance / 5) * fee_per_5_km)
    #         return shipping_fee

    #     shipping_fee = calculate_shipping_fee(distance)
        
    #     # if request.user.is_authenticated:
    #     #     user_id = request.user.id
    #     # else:
    #     #     user_id = None

    #     response_text = f'Distance: {distance} km\nShipping Fee: {shipping_fee}'

    #     return HttpResponse(response_text)

    # else:
    #     return HttpResponse('Invalid Request', status=400)
