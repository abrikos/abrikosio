from rest_framework.routers import DefaultRouter
from django.urls import path, include
from post.posts_views import  PostsViewSet

router = DefaultRouter()
router.register("", PostsViewSet, basename="pages")

urlpatterns = [
    *router.urls,
]