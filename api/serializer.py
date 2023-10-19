from rest_framework import serializers
from product.models import Product
from Cart.models import Cart
from Location.models import Location
from order.models import Order
from delivery.models import Delivery
from useraccount.models import UserAccount
from phonenumber_field.serializerfields import PhoneNumberField



# ProductSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"

# CartSerializer

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields="__all__"



# OrderSerializer

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


# Location Serializer

class CompanyLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'



class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'


# class UserAccountSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField()
#     phone_number = PhoneNumberField()

#     class Meta:
#         model = UserAccount
#         fields = ['email', 'phone_number', 'password', 'confirm_password', 'username']
#         extra_kwargs = {
#             'password': {'write_only': True},
#             'confirm_password': {'write_only': True}
#         }

#     def create(self, validated_data):
#         confirm_password = validated_data.pop('confirm_password')
#         if validated_data['password'] != confirm_password:
#             raise serializers.ValidationError("Passwords do not match.")
#         user = UserAccount(**validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user



class UserAccountSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    phone_number = PhoneNumberField()

    class Meta:
        model = UserAccount
        fields = ['email', 'phone_number', 'password', 'confirm_password', 'username']
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserAccount(**validated_data)
        user.set_password(password)
        user.save()
        return user

