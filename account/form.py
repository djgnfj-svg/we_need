

from django import forms
from django.http import HttpResponse
from django.shortcuts import render

from account.models import MyUser
from django.utils.translation import gettext_lazy as _

class RegisterForm(forms.Form):
    nickname = forms.CharField(label='닉네임',
                            widget=forms.TextInput(attrs={"id" : "input_filed", "placeholder" : "홍길동"}))
    email = forms.EmailField(label='이메일',
                            error_messages={'invalid': '유효한 이메일 주소를 입력해주세요.'},
                            widget=forms.EmailInput(attrs={"id" : "input_filed", "placeholder" : "abcd@efgh.com"}))
    password = forms.CharField(label='비밀번호',
                            min_length=6, max_length=20,
                            widget=forms.PasswordInput(attrs={"id" : "input_filed", "placeholder" : "*********"}))
    password2 = forms.CharField(label='비밀번호',
                            min_length=6, max_length=20,
                            widget=forms.PasswordInput(attrs={"id" : "input_filed", "placeholder" : "*********"}))

    # nickname = forms.CharField(label='닉네임', min_length=2, max_length=10)
    # profile_image = forms.ImageField(label='프로필 사진', required=False)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password and password2:
            if password != password2:
                raise forms.ValidationError(_("비밀번호가 일치하지 않습니다."), code="no same")

        return cleaned_data

class SignInForm(forms.Form):
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
