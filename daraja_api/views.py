from django.shortcuts import render
from django.http import JsonResponse
from .stkPush import initiate_stk_push
from .generateAcesstoken import get_access_token
from .query import query_stk_status
from .callback import process_stk_callback
from Cart.models import Cart
from .serializer import PaymentSerializer
from .stkPush import initiate_stk_push
from useraccount.models import UserAccount
import logging
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class DarajaApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = PaymentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            phone = serializer.validated_data.get('phone_number')

            user = request.user
            breakpoint()

            cart = Cart.objects.filter(user=user).first()

            if cart:

                total_amount = sum(item.product.price * item.quantity for item in cart.items.all())

                success = initiate_stk_push(total_amount, phone)

                if success:
                    return Response({'message': 'Payment initiated successfully'}, status=status.HTTP_201_CREATED)
                else:
                    return Response({'message': 'STK push failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({'message': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# class DarajaApiView(APIView):
#     def post(self, request):

#         logger = logging.getLogger()



#         serializer = PaymentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()

#             phone = serializer.validated_data.get('phone_number')

#             user = request.user

#             cart = Cart.objects.filter(user=user).first()

#             if cart:

#                 # total_amount = sum(item.price for item in cart.items.all())
#                 total_amount = sum(item.product.price * item.quantity for item in cart.items.all())


#                 success = initiate_stk_push(total_amount, phone)

#                 if success:
#                     return Response({'message': 'Payment initiated successfully'}, status=status.HTTP_201_CREATED)
#                 else:
#                     return Response({'message': 'STK push failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#             else:
#                 return Response({'message': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





