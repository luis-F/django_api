from .models import Stock
from rest_framework.test import APITestCase
from rest_framework import status
import json

VALE_JSON = {'id': 1, 'symbol': 'VALE3.SA'}

class StockTest(APITestCase):

    def setUp(self):
        self.stock = Stock.objects.create(id=2, symbol='PETR4.SA')
        self.stock.save()

    def tearDown(self):
        self.stock.delete()

    def test_get_symbol(self):
        self.assertEqual(self.stock.__str__(), self.stock.symbol)

    def test_get_stock(self):
        response = self.client.get('/stock')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(response.content, [{"id": 2, "symbol": "PETR4.SA"}])

    def test_post_stock(self):
        response = self.client.post('/stock', VALE_JSON, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertJSONEqual(response.content, VALE_JSON)
