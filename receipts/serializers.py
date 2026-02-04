from rest_framework import serializers

from receipts.models import Receipt, Item
from users.serializers import UserSerializer




class ItemSerializer(serializers.ModelSerializer):
    sum = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Item
        fields = 'name', 'price', 'quantity', 'sum'
        depth = 1
    def get_sum(self, obj):
        return obj.price * obj.quantity

class ReceiptSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    items = ItemSerializer(many=True, read_only=True, source='item_receipt_set')
    sum = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Receipt
        fields = "document", "operator", "place", 'id', 'date', 'address', 'org', 'user', 'fiscal', 'items', 'sum'

    def get_sum(self,obj):
        queryset = Item.objects.filter(receipt=obj)
        def value(x):
            return x['price'] * x['quantity']
        return 0 if not len(queryset) else sum(map(value, [ItemSerializer(q).data for q in queryset]))
