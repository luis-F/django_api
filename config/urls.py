from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from api import endpoints

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^api/', include(endpoints)),
]