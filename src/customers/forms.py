from django import forms

from .models import Customer

class CustomerCreateForm(forms.ModelForm):
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
			'address',
			'city',
			'county',
			'postcode',
			'country',
			'phone',
			'notes'
		]