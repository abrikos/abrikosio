from rest_framework import serializers

from users.serializers import UserSerializer, UserSerializerForUpdate
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Post
        fields = "__all__"

    def validate(self, attrs):
        if len( set(attrs).intersection({'title', 'short'})) < 2:
            raise serializers.ValidationError(
                {"title": "Title required", "short":"Short required"}
        )
        return attrs

class PostSerializerUpdate(PostSerializer):
    class Meta:
        model = Post
        fields = "title", 'body', 'image', 'published'
