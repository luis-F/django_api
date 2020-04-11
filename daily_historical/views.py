from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import DailyHistorical
from .serializers import DailyHistoricalSerializer


# Create your views here.
class DailyHistoricalView(viewsets.ModelViewSet):
    queryset = DailyHistorical.objects.all()
    serializer_class = DailyHistoricalSerializer

    def get_queryset(self):
        queryset = DailyHistorical.objects.all()

        stock_id = self.request.query_params.get('stock_id', None)
        order_by = self.request.query_params.get('order_by', None)

        if stock_id is not None:
            queryset = queryset.filter(stock_id=stock_id)
        if order_by is not None:
            queryset = queryset.order_by(order_by)

        return queryset

    def create(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        if not is_many:
            return super(BookViewSet, self).create(request, *args, **kwargs)
        else:
            serializer = self.get_serializer(
                validate_data=request.data,
                many=True
            )
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            return Response(serializer.data, status=201, headers=headers)
