from django.contrib.admin.decorators import action
from django.http.response import HttpResponse
from django.middleware.csrf import get_token
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import MyTokenObtainPairSerializer, UserSerializer


# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    """Token view"""

    serializer_class = MyTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    """User REST"""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == "create":
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]


def get_csrf(self, request, *args, **kwargs):
    print(get_token(request))
    return HttpResponse(get_token(request))