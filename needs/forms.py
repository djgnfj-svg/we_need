
from pyexpat import model
from django import forms

from needs.models import Needs


class NeedsCreateForm(forms.ModelForm):
	class Meta:
		model = Needs
		fields = ["title", "description", "categorys"]