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
    list_display = ['id','name','username','password','age','balance','profit','loss','qh']

@admin.register(LoginData)
class LoginDatamodelAdmin(admin.ModelAdmin):
    list_display = ['id','username','password']


@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display= ['id','name','cprice']

@admin.register(Pricelist)
class PricelistAdmin(admin.ModelAdmin):
    list_display= ['id','name','pprice']

@admin.register(Newslist)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','name','sdate','edate']

@admin.register(Buylist)
class BuyAdmin(admin.ModelAdmin):
    list_display = ['id','username','name','q','price']


