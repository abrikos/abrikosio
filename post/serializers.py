from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Post, Rate

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = 'value',

    def validate(self, attrs):
        if 'value' not in attrs:
            raise serializers.ValidationError("Value required")
        return attrs


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    #rates = serializers.CharField(source='rate_post_set.values', read_only=True)
    rates = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = "title", "short", "body", 'id', 'user', 'date', 'poster', 'published', 'rates'
    def validate(self, attrs):
        if 'title' not in attrs:
            raise serializers.ValidationError("Title required")
        if 'short' not in attrs:
            raise serializers.ValidationError("Short required")
        return attrs

    def get_rates(self,obj):
        queryset = Rate.objects.filter(post=obj)
        return [RateSerializer(q).data for q in queryset]

