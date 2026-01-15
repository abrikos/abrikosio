from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import MainPageView

urlpatterns = [
    path('test', MainPageView.as_view())
]
