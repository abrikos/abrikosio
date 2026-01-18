import os

from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from django.http.response import HttpResponse
from django.middleware.csrf import get_token
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import MyTokenObtainPairSerializer, UserSerializer, PasswordSerializer, UserSerializerForUpdate


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

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action == 'partial_update':
            serializer_class = UserSerializerForUpdate

        return serializer_class

    def perform_create(self, serializer):
        instance = serializer.save()
        if self.request.data['email'] == os.getenv("SUPER_USER"):
            instance.publisher = True
        instance.save()




    @action(detail=False, methods=['GET'])
    def auth(self, request, pk=None):
        return Response(UserSerializer(request.user).data)

    @action(detail=True, methods=['PUT'])
    def set_password(self, request, pk=None):

        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['POST'])
    def set_avatar(self, request, pk=None):
        user = self.get_object()
        if request.FILES:
            print(request.FILES['0'])
            user.avatar = request.FILES['0']
            user.save()
            return Response({'status': 'avatar set'})
        else:
            return Response({'error': 'wrong file'}, status=status.HTTP_400_BAD_REQUEST)
