from django.contrib import admin
from .models import Stock
from daily_historical.models import DailyHistorical

class DailyHistoricalAdmin(admin.ModelAdmin):
    list_display = ('stock', 'open', 'close', 'date')

# Register your models here.
admin.site.register(Stock)
admin.site.register(DailyHistorical, DailyHistoricalAdmin)
