from django.urls import path

from users.users_views import register, login

urlpatterns = [
    path('signup', login),
    path('register', register),
]