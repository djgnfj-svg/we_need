from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib import messages
from needs.models import Needs
from .forms import NeedsCreateForm
# Create your views here.

def home_view(request):
	needs = Needs.objects.order_by("created_at")
	return render(request, "pages/home.html", {"needs" : needs})

class NeedsListView(ListView):
	model = Needs
	template_name = 'pages/home'

class NeedsCreateView(CreateView):
	model = Needs
	fields = ['title', 'description', "categorys"]
	template_name = 'pages/needs_create.html'
	success_url = reverse_lazy("home") # 나중에 작성이 성공하면 디테일 뷰로가야됨
	login_url = reverse_lazy("login")

	def post(self, request, *args, **kwargs):
		needs = NeedsCreateForm(request.POST)
		if needs.is_valid():
			return super().post(request, *args, **kwargs)
		else:
			messages.warning(self.request, "잘못된입력이 있습니다.")
			return redirect(reverse("needs-create"))

	def form_valid(self, form):
		data = form.save(commit=False)
		data.creator_id = self.request.user.id
		data.save()
		return super().form_valid(form)


class NeedsList(ListView):
	model = Needs
	template_name = "pages/needs_list.html"
	queryset = Needs.objects.order_by("created_at")