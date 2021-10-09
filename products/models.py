from django.db import models
import uuid


PRODUCT_TYPE_CHOICES = [
    ('eletronic', 'Eletronic'),
    ('home_appliances', 'Home Appliances'),
    ('mobile', 'Mobile')
]


class Product(models.Model):
    code = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    type = models.CharField(
        max_length=255, choices=PRODUCT_TYPE_CHOICES)
    supplier_value = models.FloatField()
    stock_quantity = models.IntegerField()
