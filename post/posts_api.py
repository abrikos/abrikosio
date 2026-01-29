# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .models import Post, Rate
from .permissions import IsPublisher
from .serializers import PostSerializer,  RateSerializer
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class PostViewSet2(viewsets.ViewSet):
    pass
class PostViewSet(viewsets.ModelViewSet):
    """Post REST"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering = ['-created_at']

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        print('Post api action:',self.action)
        if self.action in ("list", 'retrieve'):
            permission_classes = []
        elif self.action in 'user_posts':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsPublisher]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        return Response(PostSerializer(Post.objects.filter(published=True), many=True).data)


    @action(detail=False, methods=['GET'])
    def user_posts(self, *args, **kwargs):
        user = self.request.user
        return Response(PostSerializer(Post.objects.filter(user=user), many=True).data)

class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']
    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.request.data['post'])
        serializer.save(user=self.request.user, post=post)