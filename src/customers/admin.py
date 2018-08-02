from django.contrib import admin

from .models import Customer, Address

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	# fields = ('name', 'phone', 'active') ... use to define whats in the view
	# exclude ... to define whats left out
	list_display = ('name', 'phone', 'address', 'active') # to define what gets includes in the display list
		

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
	list_display = ('street', 'city', 'postcode')
