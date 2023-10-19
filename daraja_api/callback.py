import json
from django.http import JsonResponse
from payment.models import Payment


def process_stk_callback(request):
    if request.method == 'POST':
        try:
            stk_callback_response = json.loads(request.body.decode('utf-8'))
            log_file = "Mpesastkresponse.json"
            with open(log_file, "a") as log:
                json.dump(stk_callback_response, log)

            merchant_request_id = stk_callback_response['Body']['stkCallback']['MerchantRequestID']
            checkout_request_id = stk_callback_response['Body']['stkCallback']['CheckoutRequestID']
            result_code = stk_callback_response['Body']['stkCallback']['ResultCode']
            result_desc = stk_callback_response['Body']['stkCallback']['ResultDesc']
            amount = stk_callback_response['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value']
            transaction_id = stk_callback_response['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value']
            user_phone_number = stk_callback_response['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value']

            if result_code == '0':
                payment = Payment(user_phone_number=user_phone_number,amount=amount,transaction_id=transaction_id  )
                payment.save()
                print('Payment successful')

                return JsonResponse({'message': 'Payment confirmed and transaction completed'})
            else:

                return JsonResponse({'message': f'Payment not confirmed: {result_desc}'}, status=400)
        except json.JSONDecodeError as e:
            return JsonResponse({'message': 'Invalid JSON data in callback request'}, status=400)
    elif request.method == 'GET':
        
        return JsonResponse({'message': 'This endpoint expects POST requests for processing M-Pesa STK callbacks.'})
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)




