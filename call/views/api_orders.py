from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status, viewsets
from call.serializers.orders_serializers import OrdersSerializer

class OrdersViewSet(viewsets.ModelViewSet):
    serializer_class = OrdersSerializer
    
    def get_queryset(self):
        return Orders.objects.all()
    def perform_create(self,serializer):
        order_user = self.request.user
        print(self.request.user)
        serializer.save(order_user = order_user)
