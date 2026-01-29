from django.shortcuts import render
from rest_framework import viewsets, status,exceptions
from rest_framework.decorators import action

class UserViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['GET'])
    def register(self, request, *args, **kwargs):
        return render(request, "register.pug")

    @action(detail=False, methods=['GET'])
    def login(self, request, *args, **kwargs):
        return render(request, "login.pug")

