from django.shortcuts import render
from .models import Price, Stock
from django.http import Http404

from apis.serializers import PriceSerializer, StockSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class PriceList(APIView):

	def get(self,request,format=None):
		prices = Price.objects.all()[:800]
		serializer = PriceSerializer(prices, many=True)
		return Response(serializer.data)

class StockList(APIView):

	def get(self,request,format=None):
		stocks = Stock.objects.all()
		serializer = StockSerializer(stocks, many=True)
		return Response(serializer.data)

class StockSearch(APIView):

	def get(self,request,args,format=None):
		if Stock.objects.filter(symbol= args).exists():
			stocks = Stock.objects.filter(symbol= args)
			serializer = StockSerializer(stocks, many=True)
			return Response(serializer.data)

		stocks = Stock.objects.filter(name= args)
		serializer = StockSerializer(stocks, many=True)
		return Response(serializer.data)

class PriceDetails(APIView):

	def get(self,request,args,format=None):
		
		if Price.objects.filter(symbol= args).exists():
			prices = Price.objects.filter(symbol= args)
			serializer = PriceSerializer(prices, many=True)
			return Response(serializer.data)

		return Response(status=status.HTTP_204_NO_CONTENT)
		
		'''stock_name = args
		stocks = Stock.objects.filter(name= stock_name).distinct()
		stock_symbol = stocks.symbol
		prices = Price.objects.filter(symbol= stock_symbol)
		serializer = PriceSerializer(prices, many=True)
		return Response(serializer.data)'''


