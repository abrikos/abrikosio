from rest_framework import serializers

from users.serializers import UserSerializer, UserSerializerForUpdate
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Post
        fields = "title", "short", "body", 'id', 'user', 'date', 'poster', 'published'
    def validate(self, attrs):
        if 'title' not in attrs:
            raise serializers.ValidationError("Title required")
        if 'short' not in attrs:
            raise serializers.ValidationError("Short required")
        return attrs

class PostSerializerUpdate(PostSerializer):
    class Meta:
        model = Post
        fields = "title", 'body', 'image', 'published'
