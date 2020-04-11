from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from daily_historical.views import DailyHistoricalView
from stock.views import StockView

router = routers.DefaultRouter(trailing_slash=False)
router.register('daily_historical', DailyHistoricalView)
router.register('stock', StockView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
