from django import forms

from .models import Note


class NoteModelForm(forms.ModelForm):
	# put overrides on default behaviour in here
	content = forms.CharField(
					widget=forms.Textarea(
							attrs={
								"placeholder": "Enter customer notes here",
								"rows": 5
							}
						)
					)
	class Meta:
		model = Note
		fields = [
			'content'
		]
