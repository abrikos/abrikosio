import os

import requests
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, status,exceptions
from rest_framework.decorators import action


def home(request, *args, **kwargs):
    context = {'title': 'i.o.Abrikos', }
    return render(request, template_name='index.html', context=context)


class PagesViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['GET'])
    def about(self, request, *args, **kwargs):
        context = {'title':'About', }
        return render(request, template_name='index.html', context=context )


def clash(request):
    url = os.getenv('CLASH')
    response = requests.get(url)
    return HttpResponse(response.text)