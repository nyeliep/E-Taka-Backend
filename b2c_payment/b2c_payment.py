from datetime import datetime
import json
import base64
import requests
from django.http import JsonResponse
from .generateAccessToken import get_access_token

def initiate_b2c_payment(amount, recipient_phone):
    if amount is None or recipient_phone is None:
        return JsonResponse({'error': 'Amount and recipient phone are required parameters.'}, status=400)

    try:
        access_token_response = get_access_token()
        if isinstance(access_token_response, JsonResponse):
            access_token_json = access_token_response.json()
            access_token = access_token_json.get('access_token')
            if access_token:
                business_short_code = 'YOUR_BUSINESS_SHORT_CODE'
                transaction_desc = 'B2C payment'
                process_request_url = 'https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest'

                timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
                password = base64.b64encode((business_short_code + 'YOUR_PASSKEY' + timestamp).encode()).decode()

                b2c_headers = {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + access_token
                }

                b2c_payload = {
                    'InitiatorName': 'YOUR_INITIATOR_NAME',
                    'SecurityCredential': 'YOUR_SECURITY_CREDENTIAL',
                    'CommandID': 'BusinessPayment',
                    'Amount': amount,
                    'PartyA': business_short_code,
                    'PartyB': recipient_phone,
                    'Remarks': transaction_desc,
                    'QueueTimeOutURL': 'YOUR_QUEUE_TIMEOUT_URL',
                    'ResultURL': 'YOUR_RESULT_URL',
                    'Occasion': transaction_desc
                }

                response = requests.post(process_request_url, headers=b2c_headers, json=b2c_payload)
                response.raise_for_status()
                response_data = response.json()
                response_code = response_data.get('ResponseCode')

                if response_code == '0':
                    return JsonResponse({'TransactionCompleted': 'Payment successful'})
                else:
                    return JsonResponse({'error': 'B2C payment failed'})
            else:
                return JsonResponse({'error': 'Access token not found'})
        else:
            return JsonResponse({'error': 'Failed to retrieve access token'})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse({'error': 'Failed to initiate B2C payment'})
