from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User as U

from needs.models import Needs
from ..forms import NeedsCreateForm
# Create your views here.

def home_view(request):
	# needs = get_object_or_404(Needs.objects.order_by("created_at"))
	needs = Needs.objects.order_by("created_at")
	return render(request, "pages/home.html", {"needs" : needs})

def profile_view(request, nickname):
	user_profile = U.objects.filter(nickname = nickname)
	return render(request, "pages/profile.html", {"user" : user_profile})


class NeedsListView(ListView):
	model = Needs
	template_name = 'pages/home'

	def get(self, request, *args, **kwargs):
		test = request.GET.get("test")
		_needs = Needs.objects.order_by(category=test) # 이런식
		return super().get(request, *args, **kwargs)

class NeedsCreateView(LoginRequiredMixin, CreateView):
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

class NeedsDetailView(DetailView):
	model = Needs
	template_name = "pages/needs_detail.html"
	pk_url_kwarg = 'need_id'

class NeedsUpdateView(UpdateView):
	model = Needs
	fields = ['title', 'description', "categorys", "id"]
	template_name = "pages/needs_update.html"
	pk_url_kwarg = 'need_id'
	success_url = reverse_lazy("needs-detail")

	def get_success_url(self):
		return reverse("needs-detail", kwargs={"need_id" : str(self.kwargs["need_id"])})

class NeedsDeleteView(LoginRequiredMixin, DeleteView):
	model = Needs
	success_url = reverse_lazy("needs-list")
	pk_url_kwarg = 'need_id'
	login_url = reverse_lazy('login')

	def get(self, request, *args, **kwargs):
		return self.post(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		self.object = super().get_object()
		return super().form_valid(None)

class NeedsList(ListView):
	model = Needs
	template_name = "pages/needs_list.html"
	queryset = Needs.objects.order_by("created_at")