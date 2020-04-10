from django.conf.urls import include, url
from rest_framework import routers

from .api import StockViewSet

router = routers.DefaultRouter()
router.register('historical', StockViewSet, 'historical')

urlpatterns = [
    url("^", include(router.urls)),
]
