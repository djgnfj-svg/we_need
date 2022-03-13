from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from account.models import MyUser, UserProfile
from django.contrib.auth.models import User as U
from django.contrib.auth import login, logout
from . import form

# Create your views here.
class SignUpView(FormView):
    template_name = 'pages/task_create.html'
    form_class = form.SignUpForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        nickname = form.cleaned_data['nickname']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        profile_image = form.cleaned_data['profile_image']

        user = MyUser.objects.create_user(email,email,password)
        UserProfile.objects.create(user=user,nickname=nickname,profile_image = profile_image)

        return super().form_valid(form)
        
class SignInView(FormView):
    template_name = 'pages/task_create.html'
    form_class = form.SignInForm
    success_url = reverse_lazy('home')
    
    def login(request, _user):
        login(request, _user)
        return redirect("home")

def logout_view(request):
    logout(request)
    return redirect("home")