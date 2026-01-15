from rest_framework.routers import DefaultRouter

from api.views import PostViewSet

# Описание маршрутизации для ViewSet
router = DefaultRouter()
router.register("post", PostViewSet, basename="post")

urlpatterns = router.urls

#urlpatterns+=path('admin/', FrontendTemplateView)