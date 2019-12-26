from django.db import models
from call.models import Orders
from rest_framework import serializers

class OrdersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Orders
        fields = '__all__'
        read_only_fields = ()