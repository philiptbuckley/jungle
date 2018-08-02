from django.db import models
from django.urls import reverse

# Create your models here.
class Address(models.Model):
	street 	= models.TextField(max_length=200, blank=True)
	city 	= models.CharField(max_length=50, blank=True)
	county  = models.CharField(max_length=50, blank=True)
	postcode= models.CharField(max_length=50, blank=True)
	country = models.CharField(max_length=50, default='UK')

	def __str__(self):
		return '%s, %s' % (self.street, self.city)

class Customer(models.Model):
	name 			= models.CharField(max_length=120, blank=False, null=False)
	phone			= models.CharField(max_length=50, blank=True, null=True)
	address			= models.ForeignKey(Address, on_delete=models.CASCADE)
	# inv_addr	= models.ForeignKey(Address, on_delete=models.CASCADE)
	notes			= models.TextField(blank=True)
	active			= models.BooleanField(default=False)

	# invoice contact -- needs a many-one key to a contact name/role/email/phone

	def get_absolute_url(self):
		return reverse("customers:customer-detail", kwargs={"my_id": self.id})

