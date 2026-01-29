from django.shortcuts import render


def register(request):
    return render(request, "register.pug")

def login(request):
    return render(request, "login.pug")
