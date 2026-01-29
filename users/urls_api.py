from django.urls.conf import path, include
from rest_framework.routers import DefaultRouter

from users.users_api import UserViewSet

router = DefaultRouter()
router.register("", UserViewSet, basename="users")

urlpatterns = [
    *router.urls,
]
