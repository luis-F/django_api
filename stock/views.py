from django.shortcuts import render
from rest_framework import viewsets
from .models import Stock
from .serializers import StockSerializer


# Create your views here.
class StockView(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
