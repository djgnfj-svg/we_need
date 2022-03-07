from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from account.models import MyUser
from . import form

# Create your views here.
class SigninView(CreateView):
    model = MyUser
    fields = ['title', 'type', 'due']
    template_name = 'pages/task_create.html'
    form_class = form.LoginForm()
    success_url = '/'