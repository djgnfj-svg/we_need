

from django import forms

from account.models import MyUser


class LoginForm(forms.Form):
	class Meta:
		model = MyUser
		field=(
			"email",
			"password",
		)

	email = forms.EmailField(
		max_length=100, required=False, widget=forms.EmailInput(attrs={"placeholder": "test1234@test.com"})
	)
	password = forms.CharField(
		max_length=30, required=True, 
		widget=forms.PasswordInput(attrs={})
	)
