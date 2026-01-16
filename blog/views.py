from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
import json
from django.middleware.csrf import get_token

class MainPageView(View):
    def get(self, request):
        context = {
            'post_data12': request.body,
            'get_data': json.dumps(request.GET)  # Сериализуем в JSON
        }
        return render(request, 'index.html', context)

