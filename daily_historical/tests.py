from .models import DailyHistorical
from stock.models import Stock
from rest_framework.test import APITestCase
from rest_framework import status
import json
from .utils import *


class DailyHistoricalTest(APITestCase):

    def setUp(self):
        Stock.objects.bulk_create([
            Stock(id=1, symbol="PETR4.SA"),
            Stock(id=2, symbol="CIEL3.SA"),
        ])
        DailyHistorical.objects.bulk_create([
            DailyHistorical(
                id=1,
                date="2020-04-09",
                open=17.94,
                high=18.69,
                low=16.5,
                close=16.82,
                volume=185771300.0,
                dividends=0.0,
                stock_splits=0.0,
                stock=Stock.objects.get(pk=1)
            ),
            DailyHistorical(
                id=2,
                date="2020-03-01",
                open=10.94,
                high=11.69,
                low=9.5,
                close=11.2,
                volume=182222300.0,
                dividends=0.0,
                stock_splits=0.0,
                stock=Stock.objects.get(pk=2)
            ),
        ])

    def tearDown(self):
        DailyHistorical.objects.all().delete()
        Stock.objects.all().delete()

    def test_get_daily_historical(self):
        response = self.client.get(DAILY_HISTORICAL_URL)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertJSONEqual(
            response.content, MUTIPLE_DAILY_HISTORICAL_RESPONSE)

    def test_get_daily_historical_by_id(self):
        response = self.client.get(DAILY_HISTORICAL_URL, {
                                   'stock_id': 1})

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(
            response.content, SINGLE_DAILY_HISTORICAL_RESPONSE)

    def test_get_daily_historical_order_by(self):
        response = self.client.get(DAILY_HISTORICAL_URL, {
                                   'order_by': 'date'})

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(
            response.content, MUTIPLE_DAILY_HISTORICAL_RESPONSE_ORDERED_DESC)

    def test_post_daily_historical_(self):
        request = self.client.post(
            DAILY_HISTORICAL_URL, MULTIPLE_DAILY_HISTORICAL_POST, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
