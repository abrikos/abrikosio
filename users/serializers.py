from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token


class PasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = "password", "password2"

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""

    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    email = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = 'id','email','password', 'password2', 'avatar', 'publisher', 'nickname'

    def validate(self, attrs):
        if 'password' in attrs and 'password2' in attrs:
            if attrs["password"] != attrs["password2"]:
                raise serializers.ValidationError(
                    {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        user = User.objects.create_user(
            email=validated_data["email"],
        )

        user.set_password(validated_data["password"])
        user.save()
        return user

class UserSerializerForUpdate(UserSerializer):
    class Meta:
        model = User
        fields = tuple(set(UserSerializer.Meta.fields).difference(('email', 'id', 'password', 'publisher', 'avatar')))