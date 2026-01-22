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
    rate = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = "title", "short", "body", 'id', 'user', 'date', 'poster', 'published', 'rate'

    def get_rate(self,obj):
        queryset = Rate.objects.filter(post=obj)
        def value(x):
            return x['value']
        return 0 if not len(queryset) else sum(map(value, [RateSerializer(q).data for q in queryset])) / len(queryset)
