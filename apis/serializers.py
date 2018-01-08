from .models import Price, Stock
from rest_framework import serializers

class PriceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Price
		fields = ('date','symbol','open_price','close_price','low_price','high_price','volume')

class StockSerializer(serializers.ModelSerializer):
	class Meta:
		model = Stock
		fields = ('symbol','name','market_capital','sector','industry')
		