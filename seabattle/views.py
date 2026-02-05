from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from seabattle.models import SeaBattle, SeaBattleSerializer


# Create your views here.

def check_all_ships(field:list[dict]):
    errors = []
    for ship_size in range(1,6):
        ship = list(filter(lambda x:x['ship'] == ship_size, field))
        if not len(ship):
            errors.append(f'Ship {ship_size} must be placed')
        elif len(ship) != ship_size:
            errors.append(f'Ship {ship_size} has collision')
        elif has_collision(field,ship,ship_size):
            errors.append(f'Ship {ship_size} collision')
    return errors

def has_collision(field, ship, ship_size):
    for cell in ship:
        for row in range(cell['row'] - 1, cell['row'] + 2):
            for col in range(cell['col'] - 1, cell['col'] + 2):
                idx = next((index for index, d in enumerate(field) if d['row'] == row and d['col'] == col), None)
                if idx and field[idx]['ship'] != ship_size:
                    return True
    return False

class SBApiViewSet(viewsets.GenericViewSet):
    @action(detail=False, methods=['POST'])
    def check_field(self, request):
        field = request.data
        errors = check_all_ships(field)
        if len(errors):
            return Response(errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        sb = SeaBattle(user=request.user, field_my=field, field_op=field)
        sb.save()
        return Response(SeaBattleSerializer( sb).data)
