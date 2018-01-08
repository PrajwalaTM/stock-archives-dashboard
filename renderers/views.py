from django.shortcuts import render
from django.conf import settings
from .forms import SearchStockForm
import json
import requests

# Create your views here.
def load_historical_data(request):
	r = requests.get('http://127.0.0.1:8000/apis/get_all_prices')
	json = r.json()
	historical_data = json
	#company_data = json['Time Series (Daily)']
	#serializer = PriceSerializer(data=json)
	#if serializer.is_valid():
	#	company_data = serializer.save()
	return render(request,'renderers/allHistoricalData.html',{'historical_data':historical_data})

def load_company_data(request):
	r = requests.get('http://127.0.0.1:8000/apis/get_all_stocks')
	json = r.json()
	company_data = json
	#company_data = json['Time Series (Daily)']
	#serializer = PriceSerializer(data=json)
	#if serializer.is_valid():
	#	company_data = serializer.save()
	return render(request,'renderers/allCompanyData.html',{'company_data':company_data})

def search_stock(request):
	if request.method == 'POST':
		myform = SearchStockForm(request.POST)
		if myform.is_valid():
			search_text = myform.cleaned_data['search_text']
			r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+search_text+'&apikey=27S6E8RMDPRVD4UF')
			current_stock_data = r.json()["Time Series (Daily)"]
			#current_stock_data = json.load(current_stock_data)
			value_pairs={}		
			for k,v in current_stock_data.items():
				values=[]
				values.append({"open":v['1. open']})
				values.append({"close":v['4. close']})
				values.append({"low":v['3. low']})
				values.append({"high":v['2. high']})
				values.append({"volume":v['5. volume']})
				value_pairs[k]=values
			return render(request,'renderers/searchStocks.html',{'current_stock_data':current_stock_data,'value_pairs':value_pairs})
		return render(request,'renderers/searchStocks.html')
