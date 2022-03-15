

from django import forms
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
        print("clean")
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password and password2:
            if password != password2:
                raise forms.ValidationError(_("비밀번호가 일치하지 않습니다."), code="no same")

        return cleaned_data

class LoginForm(forms.Form):
    email = forms.EmailField(label='이메일',
                            error_messages={'invalid': '유효한 이메일 주소를 입력해주세요.'},
                            widget=forms.EmailInput(attrs={"id" : "input_filed", "placeholder" : "abcd@efgh.com"}))
    password = forms.CharField(label='비밀번호',
                            min_length=6, max_length=20,
                            widget=forms.PasswordInput(attrs={"id" : "input_filed", "placeholder" : "*********"}))

