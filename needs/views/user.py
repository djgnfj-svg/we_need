from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib import auth, messages
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password
from django.views.generic import FormView

from django.contrib.auth.models import User as U
from .. import forms

def profile_view(request, nickname):
	user_profile = U.objects.filter(nickname = nickname)
	return render(request, "user/profile.html", {"user" : user_profile})

# Create your views here.
class RegisterView(FormView):
    template_name = 'user/register.html'
    form_class = forms.RegisterForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        print("form_valid")
        nickname = form.cleaned_data['nickname']
        email = form.cleaned_data['email']
        password = make_password(form.cleaned_data['password'])
        # profile_image = form.cleaned_data['profile_image']
        # UserProfile.objects.create(user=user,nickname=nickname,profile_image = profile_image)
        user = U.objects.create(email=email, password=password, username=nickname)
        login(self.request, user)
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'user/login.html'
    form_class = forms.LoginForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try :
            user = U.objects.get(email=email)
        except U.DoesNotExist:
            pass
        else :
            if user.check_password(password):
                login(self.request, user)
                return super().form_valid(form)
        messages.warning(self.request, '계정 혹은 비밀번호를 확인해 주세요')
        return redirect(reverse('login'))

def logout_view(request):
    logout(request)
    return redirect("home")