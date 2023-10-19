
from django.shortcuts import render,redirect
from rest_framework.views import APIView
from product.models import Product
from.serializer import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from api.serializer import OrderSerializer
from django.shortcuts import get_object_or_404
from order.models import Order
from rest_framework.permissions import IsAuthenticated
from Location.models import Location
from .serializer import CompanyLocationSerializer
from Cart.models import Cart
from .serializer import CartSerializer
from delivery.models import Delivery
from .serializer import DeliverySerializer
from rest_framework.decorators import api_view
from useraccount.models import UserAccount
from django.contrib.auth.models import User
from .serializer import UserAccountSerializer
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate, login, logout
from .serializer import UserAccountSerializer


# Product

class ProductListView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):
    def get(self,request,id,format=None):
        product=Product.objects.get(id=id)
        serializer=ProductSerializer(product)
        return Response(serializer.data)

    def put(self,request,id,format=None):
        product=Product.objects.get(id=id)
        serializer=ProductSerializer(product,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id,format=None):
        product=Product.objects.get(id=id)
        product.delete()
        return Response("product successfully deleted",status=status.HTTP_204_NO_CONTENT)




def create_product(request):
    product = Product()
    product.category = Product.TELEVISION
    product.save()
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_201_CREATED)



# Cart view
class CartListView(APIView):
    def get(self, request):
        cart = Cart.objects.all()
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
        return Response(serializer.data)




class OrderListView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartDetailView(APIView):
    def get(self, request, cart_id):
        cart = get_object_or_404(Cart, id=cart_id)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def put(self, request, cart_id):
        cart = get_object_or_404(Cart, id=cart_id)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, cart_id):
        cart = get_object_or_404(Cart, id=cart_id)
        cart.delete()
        return Response("Cart successfully deleted", status=status.HTTP_204_NO_CONTENT)


# Order View

class OrderDetailView(APIView):
    def get(self, request, id):
        order = get_object_or_404(Order, pk=id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, id):
        order = get_object_or_404(Order, pk=id)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        order = get_object_or_404(Order, pk=id)
        order.delete()
        return Response("Order deleted", status=status.HTTP_204_NO_CONTENT)


# Location


class CompanyLocationAPI(APIView):


        def get(self, request):
            try:
                  locations = Location.objects.all()
                  serializer = CompanyLocationSerializer(locations, many=True)
                  return Response(serializer.data, status=status.HTTP_200_OK)
            except Location.DoesNotExist:
                   return Response({'error': 'Locations not found'}, status=status.HTTP_404_NOT_FOUND)




        def post(self, request):
        # Deserialize the data from the request
            serializer = CompanyLocationSerializer(data=request.data)

            if serializer.is_valid():
                   serializer.save()
                   return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
               return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





#  Delivery view

class DeliveryList(APIView):
    def post(self, request):
        serializer = DeliverySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        deliveries = Delivery.objects.all()
        serializer = DeliverySerializer(deliveries, many=True)
        return Response(serializer.data)

class DeliveryDetail(APIView):
    def get(self, request, id):
        try:
            delivery = Delivery.objects.get(id=id)
        except Delivery.DoesNotExist:
            return Response(
                {"error": "Delivery not found", "message": "The requested delivery does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = DeliverySerializer(delivery)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            delivery = Delivery.objects.get(id=id)
        except Delivery.DoesNotExist:
            return Response(
                {"error": "Delivery not found", "message": "The requested delivery does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = DeliverySerializer(delivery, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Delivery details updated successfully",
                    "delivery_data": serializer.data
                }
            )
        else:
            return Response(
                {
                    "error": "Invalid data",
                    "errors": serializer.errors,
                    "message": "Failed to update delivery details. Please check your input and try again."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, id):
        try:
            delivery = Delivery.objects.get(id=id)
        except Delivery.DoesNotExist:
            return Response(
                {"error": "Delivery not found", "message": "The requested delivery does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )

        delivery.delete()
        return Response({"message": "Delivery deleted successfully"}, status=status.HTTP_204_NO_CONTENT)









# user view



class UserListView(APIView):

    def get(self, request):
        users = UserAccount.objects.all()
        serializer = UserAccountSerializer(users, many=True)
        return Response(serializer.data)

class UserDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            user = UserAccount.objects.get(id=id)
        except UserAccount.DoesNotExist:
            return Response(
                {"message": f"User with id {id} does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = UserAccountSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        try:
            user = UserAccount.objects.get(id=id)
        except UserAccount.DoesNotExist:
            return Response(
                {"message": f"User with id {id} does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = UserAccountSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        try:
            user = UserAccount.objects.get(id=id)
        except UserAccount.DoesNotExist:
            return Response(
                {"message": f"User with id {id} does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        user.delete()
        return Response("Customer deleted successfully", status=status.HTTP_204_NO_CONTENT)


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken

class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = UserAccount.objects.get(email=email)

        except UserAccount.DoesNotExist:
            return Response({'error': 'Email not found'}, status=status.HTTP_401_UNAUTHORIZED)

        if check_password(password, user.password):

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({'error': 'Successfully logged in.','access_token': access_token}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)








class UserLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)




from rest_framework.exceptions import ValidationError

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserAccountSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            login(request, user)
            return Response({'message': 'Successfully registered'}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            if 'username' in e.detail and 'already exists' in e.detail['username'][0]:
                return Response({'message': 'Username is already taken'}, status=status.HTTP_409_CONFLICT)
            elif 'email' in e.detail and 'already exists' in e.detail['email'][0]:
                return Response({'message': 'Email is already registered'}, status=status.HTTP_409_CONFLICT)
            elif 'password' in e.detail and 'already exists' in e.detail['password'][0]:
                return Response({'message': 'Password is already in use'}, status=status.HTTP_409_CONFLICT)
            else:
                return Response({'message': 'Please check your input fields', 'errors': e.detail}, status=status.HTTP_400_BAD_REQUEST)







