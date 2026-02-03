import json

from django.shortcuts import render
from rest_framework import viewsets, status, exceptions
from rest_framework.response import Response
from receipts.models import Receipt
from receipts.serializers import ReceiptSerializer, ItemSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.db.utils import IntegrityError


# Create your views here.
class ReceiptApiViewSet(viewsets.ModelViewSet):
    """Receipt REST"""

    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        print('Receipt api action:', self.action)
        if self.action in ["create", 'login']:
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=['POST'])
    def upload(self, request):
        print(self.request.FILES)
        file = self.request.FILES.get('file')
        if not file:
            return Response({'detail': 'No file selected'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        try:
            json_data = list(
                map(lambda x: x['ticket']['document']['receipt'], json.load(file))
            )
        except Exception as e:
            return Response({'detail': 'Wrong receipts file'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        unique_docs = []
        unique_data = []
        wrong_data = []
        for item in json_data:
            if 'fiscalDriveNumber' in item and (item['fiscalDriveNumber'] not in unique_docs):
                unique_docs.append(item['fiscalDriveNumber'])
                unique_data.append(item)
            else:
                wrong_data.append(item)
        print(len(json_data), len(wrong_data), len(unique_data))
        # return Response([])
        total = 0
        processed = 0
        for root in json_data:
            total += 1
            data = {
                'document': root['fiscalDriveNumber'],
                'operator': root['operator'] if 'operator' in root else '',
                'org': root['user'] if 'user' in root else '',
                'place': root['retailPlace'] if 'retailPlace' in root else '',
                'address': root['retailPlaceAddress'] if 'retailPlaceAddress' in root else '',
                'date': root['dateTime'].replace(' ', 'T'),
                'fiscal': root['fiscalSign']
            }
            if not Receipt.objects.filter(fiscal=data['fiscal']).exists():
                serializer = self.get_serializer(data=data)
                serializer.is_valid(raise_exception=True)
                try:
                    receipt = serializer.save(user=request.user)
                    processed += 1
                    for item in root['items']:
                        item['price'] = item['price'] / 100
                        item['name'] = item['name'].replace('\x00', '')
                        serializer2 = ItemSerializer(data=item)
                        serializer2.is_valid(raise_exception=True)
                        item = serializer2.save(receipt=receipt)
                except Exception as e:
                    return Response({"detail": e.__dict__}, status=status.HTTP_409_CONFLICT)
        return Response({'total': total, 'processed':processed})
