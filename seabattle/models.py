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
    ships = models.IntegerField(default=5)
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

    @property
    def field_op_masked(self):
        #return self.field_op
        def mask(cell):
            if 'kill' not in cell:
                cell['ship'] = ''
            #cell['isShip'] = False
            return cell
        def show_killed(cell):
            return cell['ship'] == size and 'isShip' in cell and 'hit' in cell

        for size in range(1, self.ships + 1):
            killed = list(filter(show_killed, self.field_op))
            if len(killed) == size:
                for k in killed:
                    k['kill'] = True
                print(size, killed)
        strike_ships_only = list(filter(lambda x: 'strike' in x and 'isShip' in x, self.field_op))
        strike_empty_only = list(filter(lambda x: 'strike' in x, self.field_op))
        mapped = list(map(mask, strike_ships_only + strike_empty_only))
        return mapped


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
        fields = tuple(set(SeaBattleSerializerList.Meta.fields).difference(('ZZZZ',))) + ('field_op_masked', 'field_my')

class SeaBattleSerializerOver(SeaBattleSerializerList):
    class Meta:
        model = SeaBattle
        fields = tuple(set(SeaBattleSerializerList.Meta.fields).difference(('ZZZZ',))) + ('field_op', 'field_my')

    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     # Add or modify a field in the output dictionary
    #     ret['field_op'] = list(filter(lambda x:'strike' in x, map(lambda x: x, ret['field_op'])))
    #     return ret
