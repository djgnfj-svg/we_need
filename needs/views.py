from importlib.metadata import requires
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView, DetailView, UpdateView, DeleteView, CreateView

from needs.models import Needs

# Create your views here.

def home_view(request):
	return render(request, "pages/home.html")

class NeedsCreateView(CreateView):
	model = Needs
	fields = ['title', 'description']
	template_name = 'pages/needs_create.html'
	success_url = reverse_lazy("home") # 나중에 디테일 뷰로가야됨


class NeedsList(FormView):
	model = Needs
	template_name = "pages/needs_list"
	querset = Needs.objects.filter()