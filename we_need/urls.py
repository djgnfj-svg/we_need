"""we_need URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from account.views import LoginView, RegisterView, logout_view

from needs.views import NeedsCreateView, NeedsList, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('login/', LoginView.as_view(),name="login"),
    path('register/', RegisterView.as_view(),name="register"),
    path('logout/', logout_view, name="logout"),
    # path('profile/', views.as_view(),name="profile"),
    # path('prpfile/update', views.as_view(),name="profile-update"),
    path('needs/', NeedsList.as_view(),name="needs-list"),
    path('needs/create/', NeedsCreateView.as_view(),name="needs-create"),
    # path('needs/<int:need_id>/', views.as_view(),name="needs-view"),
    # path('needs/<int:need_id>/update/', views.as_view(),name="needs-update"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
