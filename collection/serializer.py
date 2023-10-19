from rest_framework import serializers
from .models import EwasteRequest

class EwasteRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EwasteRequest
        fields = '__all__'
