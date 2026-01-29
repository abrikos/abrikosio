from rest_framework.routers import DefaultRouter
from django.urls import path, include
from post.posts_views import  PostsViewSet

router = DefaultRouter()
router.register("", PostsViewSet, basename="posts")
router.register("edit", PostsViewSet, basename="post_edit")

urlpatterns = [
    *router.urls,
]