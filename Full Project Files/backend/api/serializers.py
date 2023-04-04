from rest_framework import serializers
from .models import *

class TickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticker
        fields = '__all__'


class TickerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TickerData
        fields = '__all__'

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'

class LoginDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginData
        fields = '__all__'

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model= Watchlist
        fields = '__all__'

class PricelistSerializer(serializers.ModelSerializer):
    class Meta:
        model= Pricelist
        fields = '__all__'

# class PortfolioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Portfolio
#         fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newslist
        fields = '__all__'

class BuySerializer(serializers.ModelSerializer):
    class Meta:
        model = Buylist
        fields = '__all__'