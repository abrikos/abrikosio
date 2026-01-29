from rest_framework.routers import DefaultRouter

from users.users_views import UserViewSet

router = DefaultRouter()
router.register("", UserViewSet, basename="users")

urlpatterns = [
    *router.urls,
]