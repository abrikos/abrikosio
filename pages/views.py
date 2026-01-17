# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Post
from .permissions import IsStaffUser
from .serializers import PostSerializer



class PostViewSet(viewsets.ModelViewSet):
    """Post REST"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """

        if self.action in ("list", 'view'):
            permission_classes = []
        else:
            permission_classes = [IsStaffUser]
        return [permission() for permission in permission_classes]
