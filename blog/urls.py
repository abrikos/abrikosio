import django
from django.urls import re_path
from django.views.generic import TemplateView
from django.conf import settings

from .views import MainPageView

urlpatterns = [
    re_path(r'^.*$', TemplateView.as_view(template_name="index.html"), name='pages'),
]
