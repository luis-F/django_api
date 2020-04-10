from rest_framework import serializers

from .models import Stocks, Daily_historical

class DailyHistoricalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Daily_historical
        fields = ('date','open','high','low','close','volume','dividends','stock_splits')

class StockSerializer(serializers.ModelSerializer):
    historical_data = DailyHistoricalSerializer(many=True)
    class Meta:
        model = Stocks
        fields = ('id', 'symbol', 'historical_data')

    def create(self, validate_data):
        if len(validate_data['historical_data']) == 0:
            raise serializers.ValidationError("Necessário preenchimento dos demais campos:"
            +" date ,open ,high, low, close, volume, dividends, stock_splits")
        hist = validate_data.pop('historical_data')
        stock = Stocks.objects.create(**validate_data)
        for data in hist:
            Daily_historical.objects.create(ticker=stock, **data)
        return stock
