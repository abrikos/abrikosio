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
        if self.ship_cells_count == len(self.user_hit_ships):
            return self.user
        if self.ship_cells_count == len(self.player_hit_ships):
            return self.player
        return False

    @property
    def ship_cells_count(self):
        total = 0
        for size in range(1, self.ships + 1):
            total += size
        return total

    @property
    def player_hit_ships(self):
        return list(filter(lambda x: 'strike' in x and 'isShip' in x, self.field_player))

    @property
    def user_hit_ships(self):
        return list(filter(lambda x: 'strike' in x and 'isShip' in x, self.field_user))

