from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import MainPageView, assets_file

urlpatterns = [
    path('', MainPageView.as_view()),
]
