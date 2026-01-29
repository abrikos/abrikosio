from django.urls import path
from rest_framework.routers import DefaultRouter

from .posts_api import PostViewSet, RateViewSet

# Описание маршрутизации для ViewSet
router = DefaultRouter()

router.register("rate", RateViewSet, basename="rate")
router.register("", PostViewSet, basename="post")

urlpatterns = router.urls

#urlpatterns+=path('admin/', FrontendTemplateView)