from django.urls.conf import path, include
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, get_token

router = DefaultRouter()
router.register(r"", UserViewSet, basename="users")


urlpatterns = [
    path('',include(router.urls)),
    path('token/',get_token)
]
