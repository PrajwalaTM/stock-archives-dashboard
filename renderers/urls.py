from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
	url(r'^all_company_data',views.load_company_data,name="all_company_data"),
	url(r'^all_historical_data',views.load_historical_data,name="all_historical_data"),
	url(r'^search_stock',views.search_stock,name="search_stock"),
	url(r'^',TemplateView.as_view(template_name="renderers/home.html")),
]