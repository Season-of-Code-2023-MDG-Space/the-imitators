from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Ticker)
class TickermodelAdmin(admin.ModelAdmin):
    list_display=['id','ticker_name']
@admin.register(TickerData)
class TickerDatamodelAdmin(admin.ModelAdmin):
    list_display= ['id','Ticker_name','Date','Open','High','Low','Close','AdjClose','Volume']

@admin.register(UserData)
class UserDatamodelAdmin(admin.ModelAdmin):
    list_display = ['name','username','password','age']


@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display= ['id','name','cprice']

@admin.register(Pricelist)
class PricelistAdmin(admin.ModelAdmin):
    list_display= ['id','name','pprice']
