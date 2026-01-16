from django.http.response import HttpResponse
from django.middleware.csrf import get_token
from django.shortcuts import render


def get_csrf(request):
    return HttpResponse(get_token(request))