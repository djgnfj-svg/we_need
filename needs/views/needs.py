from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User as U
from django.core.paginator import Paginator
from django.db.models import Q

from needs.models import Categories, Needs
from ..forms import NeedsCreateForm
# Create your views here.

def home_view(request):
	# needs = get_object_or_404(Needs.objects.order_by("created_at"))
	needs = Needs.objects.order_by("created_at")
	return render(request, "main/home.html", {"needs" : needs})

class NeedsListView(ListView):
	model = Needs
	template_name = 'main/home'

	def get(self, request, *args, **kwargs):
		test = request.GET.get("test")
		_needs = Needs.objects.order_by(category=test) # 이런식
		return super().get(request, *args, **kwargs)

class NeedsCreateView(LoginRequiredMixin, CreateView):
	model = Needs
	fields = ['title', 'description', "category"]
	template_name = 'need/needs_create.html'
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
	template_name = "need/needs_detail.html"
	pk_url_kwarg = 'need_id'

class NeedsUpdateView(UpdateView):
	model = Needs
	fields = ['title', 'description', "category", "id"]
	template_name = "need/needs_update.html"
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
	template_name = "need/needs_list.html"
	queryset = Needs.objects.order_by("created_at")


class SearchView(TemplateView):
	template_name = 'need/search.html'

	def get_context_data(self, **kwargs):
		page_number = self.request.GET.get('page','1')
		keyword = self.request.GET.get('keyword','')
		category_id = self.request.GET.get("category")

		query_sets = Needs.objects.all().order_by("-created_at")
		if keyword:
			query_sets = query_sets.filter(Q(title__istartswith=keyword) | Q(description__istartswith=keyword))
		if category_id:
			category = get_object_or_404(Categories, id=int(category_id))
			query_sets = query_sets.filter(category=category)
		
		needs = query_sets.all()
		paginator = Paginator(needs, 12)
		categories = Categories.objects.all()

		paging = paginator.get_page(page_number)
		return {
			'paging' : paging,
			'categories' : categories,
		}