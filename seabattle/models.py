from django.conf import settings
from django.db import models
from rest_framework import serializers

from users.serializers import UserSerializer


# Create your models here.
class SeaBattle(models.Model):
    """Sea battle model"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="sea_battle_user_set",
        null=True,
        blank=True
    )
    player = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="sea_battle_player_set",
        null=True,
        blank=True
    )
    field_user = models.JSONField(default=list)
    field_player = models.JSONField(default=list)
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
        return bool(len(self.field_user)) and bool(len(self.field_player))

    @property
    def winner(self):
        if self.ship_cells_count == self.user_killed_ships:
            return self.user
        if self.ship_cells_count == self.player_killed_ships:
            return self.player
        return False

    @property
    def ship_cells_count(self):
        total = 0
        for size in range(1, self.ships + 1):
            total += size
        return total

    @property
    def player_killed_ships(self):
        return len(list(filter(lambda x: 'strike' in x and 'isShip' in x, self.field_player)))

    @property
    def user_killed_ships(self):
        return len(list(filter(lambda x: 'strike' in x and 'isShip' in x, self.field_user)))

class SeaBattleSerializerList(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    player = UserSerializer(many=False, read_only=True)

    class Meta:
        model = SeaBattle
        fields = ['id', 'rows', 'cols', 'date', 'is_active', 'user', 'player']


class SeaBattleSerializerCreate(serializers.ModelSerializer):
    player = UserSerializer(many=False, write_only=True)
    class Meta:
        model = SeaBattle
        fields = ['id', 'player']


def field_op_masked(obj, field):
    if obj.winner:
        return field
    def mask(cell):
        if 'kill' not in cell:
            cell['ship'] = ''
        # cell['isShip'] = False
        return cell

    # def show_killed(cell):
    #     return cell['ship'] == size and 'isShip' in cell and 'hit' in cell
    #
    # for size in range(1, obj.ships + 1):
    #     killed = list(filter(show_killed, field))
    #     if len(killed) == size:
    #         for k in killed:
    #             k['kill'] = True
    #         print(size, killed)
    strike_ships_only = list(filter(lambda x: 'strike' in x and 'isShip' in x, field))
    strike_empty_only = list(filter(lambda x: 'strike' in x, field))
    mapped = list(map(mask, strike_ships_only + strike_empty_only))
    return mapped

def field_set_hit(field):
    def hit_cell(cell):
        if 'isShip' in cell and 'strike' in cell:
            cell['hit'] = True
        return cell
    hits = list(map(hit_cell, field))
    return hits

class SeaBattleSerializerPlay(SeaBattleSerializerList):
    field_op = serializers.SerializerMethodField(read_only=True)
    field_my = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = SeaBattle
        fields = tuple(set(SeaBattleSerializerList.Meta.fields).difference(('ZZZZ',))) + ('field_op', 'field_my','field_user', 'field_player')

    def get_field_my(self, obj):
        user = self.context.get("request").user
        if user == obj.user:
            return field_set_hit(obj.field_user)
        else:
            return field_set_hit(obj.field_player)

    def get_field_op(self, obj):
        user = self.context.get("request").user
        if user == obj.user:
            return field_op_masked(obj, field_set_hit(obj.field_player))
        else:
            return field_op_masked(obj, field_set_hit(obj.field_user))


class SeaBattleSerializerOver(SeaBattleSerializerList):
    class Meta:
        model = SeaBattle
        fields = tuple(set(SeaBattleSerializerList.Meta.fields).difference(('ZZZZ',))) + ('field_player', 'field_user')

    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     # Add or modify a field in the output dictionary
    #     ret['field_op'] = list(filter(lambda x:'strike' in x, map(lambda x: x, ret['field_op'])))
    #     return ret
