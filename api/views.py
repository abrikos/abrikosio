# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import Post
from api.serializers import PostSerializer



class PostViewSet(viewsets.ModelViewSet):
    """Post REST"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions = [IsAuthenticated]

