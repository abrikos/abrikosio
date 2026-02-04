from rest_framework.routers import DefaultRouter
from django.urls import path, include
from pages.views import  PagesViewSet, home

router = DefaultRouter()
# router.register("pages/", PagesViewSet, basename="pages")
# router.register("games", PagesViewSet, basename="games")

urlpatterns = [
    path("", home),
    path("games/", home),
    *router.urls,
]