
from django import forms


class NeedsCreateForm(forms.Form):
	def clean(self):
			return super().clean()