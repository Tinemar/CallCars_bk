from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status, viewsets
from call.serializers.orders_serializers import OrdersSerializer


class OrdersViewSet(viewsets.ModelViewSet):
    serializer_class = OrdersSerializer

    def get_queryset(self):
        return HttpResponse("Hello, world.")
    def perform_create(self):
        return 