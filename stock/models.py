from django.db import models


class Stock(models.Model):
    class Meta:
        db_table = 'stock'

    symbol = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.symbol
