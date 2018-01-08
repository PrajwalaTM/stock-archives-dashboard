from django.conf.urls import url,include
from apis import views

urlpatterns = [
	url(r'^get_all_prices',views.PriceList.as_view()),
	url(r'^get_all_stocks',views.StockList.as_view()),
	url(r'^get_stocks/(?P<args>[-.,\w\s]+)/',views.StockSearch.as_view()),
	url(r'^get_price_details/(?P<args>[-.,\w\s]+)/',views.PriceDetails.as_view()),

]
