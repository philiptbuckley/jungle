from django.db import models
from django.urls import reverse

# Create your models here.
class Customer(models.Model):
	name 	= models.CharField(max_length=120, blank=False, null=False)
	phone	= models.CharField(max_length=50)
	address = models.TextField(max_length=200, blank=True)
	city 	= models.CharField(max_length=50, blank=True)
	county  = models.CharField(max_length=50, blank=True)
	postcode= models.CharField(max_length=50, blank=True)
	country = models.CharField(max_length=50, default='UK')
	notes	= models.TextField(blank=True)
	active	= models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse("customers:customer-detail", kwargs={"my_id": self.id})

