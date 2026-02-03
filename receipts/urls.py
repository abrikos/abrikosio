from django.urls.conf import path, include
from rest_framework.routers import DefaultRouter

from receipts.views import ReceiptApiViewSet

router = DefaultRouter()
router.register("", ReceiptApiViewSet, basename="receipts")

urlpatterns = [
    *router.urls,
]
