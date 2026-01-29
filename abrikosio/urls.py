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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.views.generic.base import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView

from users.users_api import MyTokenObtainPairView
from .views import get_sysinfo

urlpatterns = [
    path('', include("pages.urls")),
    path('admin/', admin.site.urls),
    path("api/posts/", include("post.urls_posts_api")),
    path("posts/", include("post.urls_posts_views")),
    path("api/users/", include("users.urls_users_api")),
    path("users/", include("users.urls_users_views")),
    path("api/git", get_sysinfo),
    #path("api/auth/me", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    #path("api/auth/refresh/", MyTokenObtainPairView.as_view(), name="token_refresh"),
    path("__reload__/", include("django_browser_reload.urls")),
]

urlpatterns +=staticfiles_urlpatterns()