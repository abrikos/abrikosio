from django.urls.conf import path, include
from rest_framework.routers import DefaultRouter

from users.users_api import UserApiViewSet

router = DefaultRouter()
router.register("", UserApiViewSet, basename="users")

urlpatterns = [
    *router.urls,
]
