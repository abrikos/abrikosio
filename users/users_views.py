from django.shortcuts import render
from rest_framework import viewsets, status,exceptions
from rest_framework.decorators import action

class UserViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['GET'])
    def register(self, request, *args, **kwargs):
        context = {'title': 'Register user'}
        return render(self.request, template_name='index.html', context=context)

    @action(detail=False, methods=['GET'])
    def login(self, request, *args, **kwargs):
        context = {'title': 'Login'}
        return render(self.request, template_name='index.html', context=context)

    @action(detail=False, methods=['GET'])
    def cabinet(self, request, *args, **kwargs):
        context = {'title': 'Login'}
        return render(self.request, template_name='index.html', context=context)

