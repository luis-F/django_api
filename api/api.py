from rest_framework import viewsets, permissions
from rest_framework.response import Response

from .serializers import StockSerializer
from .models import Stocks

class StockViewSet(viewsets.ModelViewSet):
    permissions = [permissions.AllowAny,]
    serializer_class = StockSerializer
    queryset = Stocks.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = StockSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response({
            "dados": StockSerializer(data, context=self.get_serializer_context()).data,
        })
