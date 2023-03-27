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

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model= Watchlist
        fields = '__all__'

class PricelistSerializer(serializers.ModelSerializer):
    class Meta:
        model= Pricelist
        fields = '__all__'