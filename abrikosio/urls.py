"""
URL configuration for abrikosio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views import static
from django.conf import settings
from django.views.generic.base import RedirectView
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import MyTokenObtainPairView
from .views import get_csrf

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path("api/", include("api.urls")),
    path("user/", include("users.urls")),
    path("pages/", include("blog.urls")),
    path("csrf_token/", get_csrf),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", MyTokenObtainPairView.as_view(), name="token_refresh"),
    path('', RedirectView.as_view(pattern_name='pages', permanent=False))
    #path(r'^assets/(?P<path>.*)$', static.serve, {'document_root': settings.BASE_DIR + "/assets"}),

]
