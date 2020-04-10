from rest_framework import serializers
from .models import DailyHistorical
from stock.models import Stock


class DailyHistoricalSerializer(serializers.ModelSerializer):
    stockId = serializers.PrimaryKeyRelatedField(
        queryset=Stock.objects.all(),
        source='stock'
    )
    stockSplits = serializers.FloatField(source='stock_splits')

    class Meta:
        model = DailyHistorical
        fields = [
            'id',
            'stockId',
            'date',
            'open',
            'high',
            'low',
            'close',
            'volume',
            'dividends',
            'stockSplits'
        ]

#  def create(self, validate_data):
#         if len(validate_data['historical_data']) == 0:
#             raise serializers.ValidationError("Necessário preenchimento dos demais campos:"
#             +" date ,open ,high, low, close, volume, dividends, stock_splits")
#         hist = validate_data.pop('historical_data')
#         stock = Stocks.objects.create(**validate_data)
#         for data in hist:
#             Daily_historical.objects.create(ticker=stock, **data)
#         return stock
