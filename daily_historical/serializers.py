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
