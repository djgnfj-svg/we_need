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

from needs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name="home"),
    # path('sign in/', views.as_view(),name="sign in"),
    # path('sign up/', views.as_view(),name="sign up"),
    # path('profile/', views.as_view(),name="profile"),
    # path('prpfile/update', views.as_view(),name="profile-update"),
    # path('needs/', views.as_view(),name="needs-all"),
    # path('needs/<int:need_id>/', views.as_view(),name="needs-view"),
    # path('needs/<int:need_id>/create/', views.as_view(),name="needs-create"),
    # path('needs/<int:need_id>/update/', views.as_view(),name="needs-update"),


    path('test/', views.test_view, name="test"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
