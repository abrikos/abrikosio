from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
import json
import os
from django.conf import settings
import pathlib


class MainPageView(View):
    def get(self, request):
        context = {
            'post_data': request.body,
            'get_data': json.dumps(request.GET)  # Сериализуем в JSON
        }

        return render(request, 'index.html', context)

def assets_file(request, file):
    path = os.path.join(settings.BASE_DIR,'blog/templates/assets' ,file)
    suffix = pathlib.Path(file).suffix
    print(request, file, suffix)
    type = 'css' if suffix=='.css' else 'javascript'
    return HttpResponse(open(path), content_type=f'text/{type}')
