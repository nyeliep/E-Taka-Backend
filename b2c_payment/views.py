from django.shortcuts import render
from django.http import JsonResponse
from .b2c_payment import initiate_b2c_payment

def initiate_b2c_payment_view(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        recipient_phone = request.POST.get('recipient_phone')

        response = initiate_b2c_payment(amount, recipient_phone)

        return response

    return JsonResponse({'error': 'Invalid request method'}, status=400)
