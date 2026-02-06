import copy
import math
import random

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from seabattle.models import SeaBattle, SeaBattleSerializerCreate, SeaBattleSerializerPlay, SeaBattleSerializerList


# Create your views here.
class Cell:
    def __init__(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])


def check_all_ships(field: list[dict]):
    errors = []
    if not isinstance(field, list):
        errors.append('Wrong field data')
    else:
        for ship_size in range(1, 6):
            ship = list(filter(lambda x: x['ship'] == ship_size, field))
            if not len(ship):
                errors.append(f'Ship {ship_size} must be placed')
            elif len(ship) != ship_size:
                errors.append(f'The ship {ship_size} has wrong length ({len(ship)})')
            elif has_collision(field, ship, ship_size):
                errors.append(f'The ship {ship_size} is in contact with another')
    return errors


def has_collision(field, ship, ship_size):
    for cell in ship:
        for row in range(cell['row'] - 1, cell['row'] + 2):
            for col in range(cell['col'] - 1, cell['col'] + 2):
                idx = next((index for index, d in enumerate(field) if d['row'] == row and d['col'] == col), None)
                if idx and field[idx]['ship'] != ship_size:
                    return True
    return False


def fill_field(sb):
    return list(map(lambda x: {'row': math.floor(x / sb.cols), 'col': x % sb.rows, 'index': x}, [i for i in range(sb.rows * sb.cols)]))


def get_ship_cells(args, sb):
    ship = []
    if args['horizontal']:
        for col in range(args['col'], args['col'] + args['ship']):
            cell = copy.copy(args)
            cell['col'] = col
            cell['index'] = cell['row'] * sb.cols + cell['col']
            ship.append(cell)
    else:
        for row in range(args['row'], args['row'] + args['ship']):
            cell = copy.copy(args)
            cell['row'] = row
            cell['index'] = cell['row'] * sb.cols + cell['col']
            ship.append(cell)
    return ship


def validate_cell(cell, field, sb):
    if 'ship' in cell:
        return False
    ship_cells = get_ship_cells(cell, sb)
    for ship in ship_cells:
        cell = found_in_field(field, ship)
        if not cell or cell['ship']:
            return False
    return len(ship_cells)


def make_borders(field, ship):
    borders = []
    for cell in ship:
        for row in range(cell['row'] - 1, cell['row'] + 2):
            for col in range(cell['col'] - 1, cell['col'] + 2):
                found = found_in_field(field, {'row': row, 'col': col})
                if found and not 'ship' in found:
                    found['ship'] = ship[0]['ship']
                    borders.append(found)
    return borders


def found_in_field(field, cell):
    return next((c for c in field if c['row'] == cell['row'] and c['col'] == cell['col']), None)


def place_random_ships(sb):
    def check_collision(c):
        if horizontal:
            for col in range(c['col'], c['col'] + ship_size + 1):
                f = found_in_field(field_cut_borders, {'row': c['row'], 'col': col})
                if f and 'ship' in f:
                    return False
        else:
            for row in range(c['row'], c['row'] + ship_size + 1):
                f = found_in_field(field_cut_borders, {'row': row, 'col': c['col']})
                if f and 'ship' in f:
                    return False
        return True

    is_horizontal = [True, False]
    field = fill_field(sb)
    ships = []
    for ship_size in range(1, 6):
        horizontal = random.choice(is_horizontal)
        field_no_ship = list(filter(lambda x: 'ship' not in x, field))
        field_cut_borders = list(filter(lambda x: x['col'] + ship_size <= sb.cols if horizontal else x['row'] + ship_size <= sb.rows, field))
        field_no_collision = list(filter(check_collision, field_cut_borders))

        field_free = field_no_collision
        cell = random.choice(field_free)
        cell['ship'] = ship_size
        cell['isShip'] = True
        cell['horizontal'] = horizontal
        ship = get_ship_cells(cell, sb)
        borders = make_borders(field, ship)
        ships += ship + borders

    return ships


class SBApiViewSet(viewsets.GenericViewSet):
    queryset = SeaBattle.objects.all()
    serializer_class = SeaBattleSerializerList

    # @action(detail=False, methods=['GET'])
    def list(self, request):
        return Response(SeaBattleSerializerList(self.queryset, many=True).data)

    @action(detail=True, methods=['GET'], permission_classes=[IsAuthenticated])
    def random(self, request, pk=None):
        sb = SeaBattle.objects.get(pk=pk, user=request.user)
        sb.field_my = place_random_ships(sb)
        return Response(SeaBattleSerializerPlay(sb).data)

    @action(detail=True, methods=['GET'])
    def play(self, request, pk=None):
        sb = SeaBattle.objects.get(pk=pk, user=request.user)
        return Response(SeaBattleSerializerPlay(sb).data)

    @action(detail=False, methods=['GET'])
    def start(self, request):
        sb = SeaBattle(user=request.user)
        sb.save()
        return Response(SeaBattleSerializerCreate(sb).data)

    @action(detail=False, methods=['POST'])
    def check_field(self, request):
        field = request.data
        errors = check_all_ships(field)
        if len(errors):
            return Response(errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        sb = SeaBattle(user=request.user, field_my=field, field_op=field)
        sb.save()
        return Response(SeaBattleSerializerCreate(sb).data)
