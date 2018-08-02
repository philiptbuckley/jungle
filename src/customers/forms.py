from django import forms

from .models import Customer, Address

class AddressForm(forms.ModelForm):
	# put overrides on default behaviour in here
	class Meta:
		model = Address
		fields = [
			'street',
			'city',
			'county',
			'postcode',
			'country',
		]

class CustomerForm(forms.ModelForm):
	# put overrides on default behaviour in here
	notes = forms.CharField(
					widget=forms.Textarea(
							attrs={
								"placeholder": "Enter customer notes here",
								"rows": 5
							}
						)
					)
	class Meta:
		model = Customer
		fields = [
			'name',
			'phone',
			'address',
			# 'inv_addr',
			'notes',
			'active'
		]
