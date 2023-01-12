from django.shortcuts import render
from django.utils import timezone
from .models import Order
from rest_framework import viewsets
from .serializers import OrderSerializer
# Create your views here.


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        queryset = Order.objects.all()
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(order_date__range=[start_date, end_date])
            print(queryset)
        return queryset