from django.urls import path



urlpatterns = [
	path("needs",needs_view, name="api_needs")
]