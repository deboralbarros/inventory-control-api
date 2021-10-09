from django.db import models
from django.db.models.deletion import CASCADE

from products.models import Product


MOVEMENT_TYPE_CHOICES = [
    ('out', 'Output'),
    ('in', 'Input')
]


class Movement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, choices=MOVEMENT_TYPE_CHOICES)
    sale_value = models.FloatField()
    sale_data = models.DateField()
    quantity = models.IntegerField()
