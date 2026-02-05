from rest_framework.routers import DefaultRouter

from seabattle.views import SBApiViewSet

router = DefaultRouter()
router.register("", SBApiViewSet, basename="sea_battle")

urlpatterns = [
    *router.urls,
]
