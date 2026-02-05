from django.conf import settings
from django.db import models
from rest_framework import serializers


# Create your models here.
class SeaBattle(models.Model):
    """Sea battle model"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sea_battle_user_set",
    )
    field_my = models.JSONField(default=dict)
    field_op = models.JSONField(default=dict)
    rows = models.IntegerField(default=10)
    cols = models.IntegerField(default=10)

class SeaBattleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeaBattle
        fields = ['id', 'field_my', 'field_op', 'rows', 'cols']