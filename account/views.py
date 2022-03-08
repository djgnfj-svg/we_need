from django.shortcuts import redirect, render
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from account.models import MyUser

from django.contrib.auth import login, logout
from . import form

# Create your views here.
class SigninView(CreateView):
    model = MyUser
    fields = ['title', 'type', 'due']
    template_name = 'pages/task_create.html'
    form_class = form.LoginForm()
    success_url = '/'
    
    def login(request, _user):
        login(request, _user)
        return redirect("home")

def logout_view(request):
    logout(request)
    return redirect("home")