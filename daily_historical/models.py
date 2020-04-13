from django.db import models
from stock.models import Stock


class DailyHistorical(models.Model):
    class Meta:
        db_table = 'daily_historical'

    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.FloatField()
    dividends = models.FloatField()
    stock_splits = models.FloatField()
    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE
    )
