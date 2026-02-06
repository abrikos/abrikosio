from django.conf import settings
from django.db import models
from rest_framework import serializers

from users.serializers import UserSerializer


# Create your models here.
class SeaBattle(models.Model):
    """Sea battle model"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sea_battle_user_set",
    )
    field_my = models.JSONField(default=list)
    field_op = models.JSONField(default=list)
    rows = models.IntegerField(default=10)
    cols = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.user.nickname + self.date

    @property
    def date(self):
        return self.created_at.strftime("%Y-%m-%d, %H:%M:%S")

    @property
    def is_active(self):
        return bool(len(self.field_my)) and bool(len(self.field_op))

class SeaBattleSerializerList(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = SeaBattle
        fields = ['id', 'rows', 'cols', 'date', 'is_active', 'user']

class SeaBattleSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = SeaBattle
        fields = ['id']

class SeaBattleSerializerPlay(SeaBattleSerializerList):
    class Meta:
        model = SeaBattle
        fields = tuple(set(SeaBattleSerializerList.Meta.fields).difference(('ZZZZ',))) + ('field_op', 'field_my')

