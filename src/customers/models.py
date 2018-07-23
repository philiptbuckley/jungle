from django.db import models

# Create your models here.
class Customer(models.Model):
	name 	= models.CharField(max_length=120, blank=False, null=False)
	address = models.TextField(max_length=200, blank=True)
	city 	= models.CharField(max_length=50, blank=True)
	county  = models.CharField(max_length=50, blank=True)
	postcode= models.CharField(max_length=50, blank=True)
	country = models.CharField(max_length=50, default='UK')
	phone	= models.CharField(max_length=50)
	notes	= models.TextField(blank=True)