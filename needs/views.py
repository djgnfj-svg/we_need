from importlib.metadata import requires
from django.shortcuts import render

from needs.models import Needs

# Create your views here.

def home_view(request):
	return render(request, "pages/home.html")

def test_view(request):
	context = {}
	return render(request, "pages/test.html", context)