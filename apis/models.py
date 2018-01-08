from django.db import models
from django.utils import timezone

# Create your models here.

class Price(models.Model):
	date = models.DateTimeField()
	symbol = models.CharField(max_length=100)
	open_price = models.FloatField()
	close_price = models.FloatField()
	low_price = models.FloatField()
	high_price = models.FloatField()
	volume = models.BigIntegerField() 

class Stock(models.Model):
	symbol = models.CharField(max_length=100)
	name = models.CharField(max_length=500)
	market_capital = models.FloatField()
	sector = models.CharField(max_length=500)
	industry = models.CharField(max_length=1000)
