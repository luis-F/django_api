from django.shortcuts import render
from rest_framework import viewsets
from .models import DailyHistorical
from .serializers import DailyHistoricalSerializer


# Create your views here.
class DailyHistoricalView(viewsets.ModelViewSet):
    queryset = DailyHistorical.objects.all()
    serializer_class = DailyHistoricalSerializer
