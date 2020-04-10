from django.contrib import admin
from .models import Daily_historical, Stocks

class DailyHostoricalAdmin(admin.ModelAdmin):
    list_display = ('id','ticker','date','open','high','low','close','volume','dividends','stock_splits')

admin.site.register(Stocks)
admin.site.register(Daily_historical ,DailyHostoricalAdmin)
