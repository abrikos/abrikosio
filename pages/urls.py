from rest_framework.routers import DefaultRouter
from django.urls import path, include
from pages.views import  PagesViewSet, home

router = DefaultRouter()
router.register("pages/", PagesViewSet, basename="pages")

urlpatterns = [
    path("", home),
    *router.urls,
]