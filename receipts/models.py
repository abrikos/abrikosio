from django.conf import settings
from django.db import models

# Create your models here.

class Receipt(models.Model):
    """Receipt model"""
    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=['document', 'org', 'date'],
    #             name='unique_doc_org_date'
    #         )
    #     ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="receipt_user_set",
    )
    kkm = models.CharField(max_length=50, blank=True)
    operator = models.CharField(max_length=500, blank=True)
    place = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=500, blank=True)
    org = models.CharField(max_length=500, blank=True)
    fiscal = models.BigIntegerField()
    total_sum = models.FloatField(default=0)
    date = models.DateTimeField(unique=True)

class Item(models.Model):
    """Receipt item model"""
    receipt = models.ForeignKey(
        Receipt,
        on_delete=models.CASCADE,
        related_name="item_receipt_set",
    )
    name = models.CharField(max_length=500, blank=True)
    price = models.FloatField()
    quantity = models.FloatField()
