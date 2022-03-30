from django.urls import path

from rest_framework import routers

from needs.api.views import NeedsViewsSet



router = routers.DefaultRouter()
router.register(r'needs_list', NeedsViewsSet, basename="API_Needs_list")