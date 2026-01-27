import os

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import MyTokenObtainPairSerializer, UserSerializer, PasswordSerializer, UserSerializerForUpdate
from wonderwords import RandomWord


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

    def perform_list(self, request, *args, **kwargs):
        return []

    def perform_create(self, serializer):
        r = RandomWord()
        r2 = RandomWord()
        instance = serializer.save()
        if self.request.data['email'] == os.getenv("SUPER_USER"):
            instance.publisher = True
        instance.nickname = r.word() + ' ' + r2.word()
        instance.save()




    @action(detail=True, methods=['GET'])
    def me(self, request):
        return Response(UserSerializer(request.user).data)

    @action(detail=True, methods=['PATCH'])
    def set_password(self, request, pk=None):

        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['DELETE'])
    def delete_avatar(self, request, pk=None):
        user = self.get_object()
        user.avatar.delete(save=False)
        user.avatar = None
        user.save()
        return Response({'status': 'avatar deleted'})

    @action(detail=True, methods=['POST'])
    def set_avatar(self, request, pk=None):
        user = self.get_object()
        if request.FILES:
            user.avatar.delete(save=False)
            user.avatar = request.FILES['0']
            user.save()
            return Response({'status': 'avatar set'})
        else:
            return Response({'error': 'wrong file'}, status=status.HTTP_400_BAD_REQUEST)
