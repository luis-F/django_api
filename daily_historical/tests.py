from .models import DailyHistorical
from stock.models import Stock
from rest_framework.test import APITestCase
from rest_framework import status
import json
from .utils import *

class DailyHistoricalTest(APITestCase):

    def setUp(self):
        self.stock = Stock.objects.create(id=1, symbol="PETR4.SA")
        self.daily_hist = DailyHistorical.objects.create(
            id = 1,
            date = "2020-04-09",
            open = 17.94,
            high = 18.69,
            low = 16.5,
            close = 16.82,
            volume = 185771300.0,
            dividends = 0.0,
            stock_splits = 0.0,
            stock = self.stock
        )
        self.daily_hist.save()

    def tearDown(self):
        self.daily_hist.delete()
        self.stock.delete()

    def test_get_daily_historical(self):
        response = self.client.get(DAILY_HISTORICAL_URL)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(response.content, SINGLE_DAILY_HISTORICAL_RESPONSE)

    def test_get_daily_historical_by_id(self):
        response = self.client.get(DAILY_HISTORICAL_URL, {'stockId': self.stock.id})
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(response.content, SINGLE_DAILY_HISTORICAL_RESPONSE)
