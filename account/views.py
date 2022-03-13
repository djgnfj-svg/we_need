from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from account.models import MyUser, UserProfile
from django.contrib.auth.models import User as U
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt


from . import form

# Create your views here.
class SignUpView(FormView):
    template_name = 'pages/login.html'
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
        
class LoginView(FormView):
    template_name = 'pages/login.html'
    form_class = form.SignInForm
    success_url = reverse_lazy('home')
    
    def login(request, _user):
        login(request, _user)
        return redirect("home")

    @csrf_exempt
    def post(self, request):
        print(request.POST.get("email"))
        print(request.POST.get("password"))
        return super().post(request)

def logout_view(request):
    logout(request)
    return redirect("home")