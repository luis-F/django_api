from rest_framework import serializers
from .models import DailyHistorical
from stock.models import Stock


class DailyHistoricalListSerializer(serializers.ListSerializer):
    def create(self, validate_data):
        daily_data = [DailyHistorical(**item) for item in validate_data]
        return DailyHistorical.objects.bulk_create(daily_data)


class DailyHistoricalSerializer(serializers.ModelSerializer):
    stockId = serializers.PrimaryKeyRelatedField(
        queryset=Stock.objects.all(),
        source='stock'
    )
    stockSplits = serializers.FloatField(source='stock_splits')

    class Meta:
        list_serializer_class = DailyHistoricalListSerializer
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

    #  Essa parte de validação fica aqui ou no view?
    #  Tenho que fazer um if de cada um?
    # def create(self, validate_data):
    #     if len(validate_data['historical_data']) == 0:
    #         raise serializers.ValidationError("Necessário preenchimento dos demais campos:"
    #                                           + " date ,open ,high, low, close, volume, dividends, stock_splits")
    #     hist = validate_data.pop('historical_data')
    #     stock = Stocks.objects.create(**validate_data)
    #     for data in hist:
    #         Daily_historical.objects.create(ticker=stock, **data)
    #     return stock
