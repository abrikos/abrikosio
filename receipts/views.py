import json

from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status, exceptions
from rest_framework.response import Response
from receipts.models import Receipt, Item
from receipts.serializers import ReceiptSerializer, ItemSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.db.utils import IntegrityError
from django.db import connection


def dictfetchall(cursor):
    """
    Return all rows from a cursor as a list of dicts.
    """
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def get_query(sql, params=None):
    with connection.cursor() as cursor:
        try:
            cursor.execute(sql, params)
            return Response(dictfetchall(cursor))
        except Exception as e:
            print(e)
            return Response(str(e), status.HTTP_400_BAD_REQUEST)


# Create your views here.
class ReceiptApiViewSet(viewsets.GenericViewSet):
    """Receipt REST"""

    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['GET'])
    def view(self, request, pk=None):
        return Response(ReceiptSerializer(Receipt.objects.get(pk=pk)).data)

    @action(detail=False, methods=['GET'])
    def year_month(self, request, *args, **kwargs):
        year = request.query_params.get('year', None)
        month = request.query_params.get('month', None)
        sql = f"""select rr.id, rr.org, rr.address, TO_CHAR(rr.date, 'YYYY-MM-DD HH24:MI:SS') date, 
(select sum(ri.price * ri.quantity) from receipts_item ri where receipt_id=rr.id group by receipt_id) sum
from receipts_receipt rr 
where extract(year from date)=%s and extract(month from date)=%s 
group by rr.id
order by rr.date desc;
"""
        return get_query(sql, (year, month))

    @action(detail=False, methods=['GET'])
    def search(self, request, *args, **kwargs):
        s = request.query_params.get('search', None).lower()
        search = f"%{s}%"
        #return Response(ItemSerializer(Item.objects.select_related('receipt').filter(name__icontains=s)).data)
        sql = f"""select *, TO_CHAR(rr.date, 'YYYY-MM-DD HH24:MI:SS') date from receipts_item ri 
inner join receipts_receipt rr on rr.id=receipt_id
where lower(name) like lower(%s)
order by rr.date desc;
"""
        return get_query(sql, (search,))



    @action(detail=False, methods=['GET'])
    def monthly(self, request):

        sql = f"""select extract(year from date) as year, 
extract(month from date) as month, 
count(*) count , sum (ri.price * ri.quantity)
from receipts_receipt rr 
inner join receipts_item ri on ri.receipt_id=rr.id
where rr.user_id={request.user.id}
group by year, month 
order by year desc, month desc;"""
        return get_query(sql)

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
