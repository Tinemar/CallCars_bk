from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status, viewsets
from call.serializers.orders_serializers import OrdersSerializer
from call.models import Orders
import call.utils as utils

class OrdersViewSet(viewsets.ModelViewSet):
    serializer_class = OrdersSerializer
    
    def get_queryset(self):
        return Orders.objects.all()
    def perform_create(self,serializer):
        order_user = self.request.user
        user_id = self.request.user.id
        order_id = utils.create_order_id(user_id)
        serializer.save(order_user = order_user,order_id = order_id)
    def perform_update(self,serializer):
        status = self.request.data.get('status')
        driver = self.request.data.get('driver')
        driver_phone = self.request.data.get('driver_phone')
        driver_number = self.request.data.get('driver_number')
        serializer.save(status=status,driver_phone = driver_phone,driver_number = driver_number)
    def perform_delete(self,serializer)