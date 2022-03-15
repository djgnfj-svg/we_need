from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from needs.models import Needs
from .forms import NeedsCreateForm
# Create your views here.

def home_view(request):
	needs = Needs
	return render(request, "pages/home.html")

class NeedsListView(ListView):
	model = Needs
	template_name = 'pages/home'

class NeedsCreateView(CreateView):
	model = Needs
	fields = ['title', 'description', "categorys"]
	template_name = 'pages/needs_create.html'
	success_url = reverse_lazy("home") # 나중에 작성이 성공하면 디테일 뷰로가야됨
	login_url = reverse_lazy("login")

	def form_valid(self, form):
		data = form.save(commit=False)
		data.creator_id = self.request.user.id
		data.save()
		print(self.request.POST)
		print(self.kwargs[""])
		print(self.request.user.id)
		return super().form_valid(form)


class NeedsList(ListView):
	model = Needs
	template_name = "pages/needs_list.html"