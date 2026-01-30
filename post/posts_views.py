from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, status, exceptions
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from post.models import Post
from post.serializers import PostSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        try:
            post = Post.objects.get(pk=pk)

            context = {'title': post.title, 'short':post.short, 'poster':post.poster  }
            return render(self.request, template_name='index.html', context=context)
        except Exception as e:
            return HttpResponse("Not found", status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['GET'])
    def edit(self, request, *args, **kwargs):
        context = {'title': 'Edit post', }
        return render(self.request, template_name='index.html', context=context)
