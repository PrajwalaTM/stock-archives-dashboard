from django import forms

class SearchStockForm(forms.Form):
	search_text = forms.CharField(max_length=200)