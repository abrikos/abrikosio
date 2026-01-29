import os

from django.contrib.auth.hashers import check_password
from django.db.utils import IntegrityError
from django.http.response import HttpResponse
from rest_framework import viewsets, status,exceptions
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView


from users.models import User
from users.serializers import MyTokenObtainPairSerializer, UserSerializer, PasswordSerializer, UserSerializerForUpdate
from wonderwords import RandomWord

# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    """Token view"""

    serializer_class = MyTokenObtainPairSerializer


def set_cookie(user):
    refresh = RefreshToken.for_user(user)

    token = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    response = Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
    response.set_cookie('access', token['access'])
    response.set_cookie('refresh', token['refresh'])
    return response


class UserApiViewSet(viewsets.ModelViewSet):
    """User REST"""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        print('User api action:', self.action)
        if self.action in ["create", 'login']:
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action == 'partial_update':
            serializer_class = UserSerializerForUpdate

        return serializer_class


    def create(self, request, *args, **kwargs):

        r = RandomWord()
        r2 = RandomWord()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = serializer.save()

            if self.request.data['email'] == os.getenv("SUPER_USER"):
                user.publisher = True
                user.is_staff = True
                user.is_superuser = True
            user.nickname = r.word() + ' ' + r2.word()

            user.save()
            return set_cookie(user)
        except IntegrityError as e:
            return Response({"detail": "User exists"}, status=status.HTTP_409_CONFLICT)

    @action(detail=False, methods=['POST'])
    def login(self, request):
        try:
            email = request.data['email']
            password = request.data['password']
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                return set_cookie(user)
        except KeyError as e:
            raise exceptions.NotAcceptable(f'Field required: "{e}"')
        except User.DoesNotExist as e:
            raise exceptions.NotAuthenticated(e)
        return HttpResponse('Wrong credentials', status=404)

    @action(detail=False, methods=['GET'])
    def me(self, request, *args, **kwargs):
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
