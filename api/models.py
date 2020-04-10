from django.db import models

class Stocks(models.Model):
    symbol = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.symbol

class Daily_historical(models.Model):
    ticker          = models.ForeignKey(Stocks, on_delete=models.CASCADE, related_name="historical_data")
    date            = models.DateField()
    open            = models.FloatField()
    high            = models.FloatField()
    low             = models.FloatField()
    close           = models.FloatField()
    volume          = models.FloatField()
    dividends       = models.FloatField()
    stock_splits    = models.FloatField()
