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
        post = Post.objects.get(pk=pk)
        context = {'title': post.title, 'short':post.short, 'poster':post.poster  }
        return render(self.request, template_name='index.html', context=context)

    @action(detail=True, methods=['GET'])
    def edit(self):
        context = {'title': 'Edit post', }
        return render(self.request, template_name='index.html', context=context)
