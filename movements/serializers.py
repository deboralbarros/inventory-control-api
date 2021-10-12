from rest_framework import serializers

from products.models import PRODUCT_TYPE_CHOICES


class ProductSerializer(serializers.Serializer):
    code = serializers.UUIDField(read_only=True)
    description = serializers.CharField()
    type = serializers.ChoiceField(PRODUCT_TYPE_CHOICES)
    supplier_value = serializers.FloatField()
    stock_quantity = serializers.IntegerField()


class MovementSerializer(serializers.Serializer):
    product = serializers.CharField()
    type = serializers.CharField()
    sale_value = serializers.FloatField()
    sale_date = serializers.DateField()
    quantity = serializers.IntegerField()


class MovementSerializerOut(serializers.Serializer):
    id = serializers.IntegerField()
    product = ProductSerializer()
    type = serializers.CharField()
    sale_value = serializers.FloatField()
    sale_date = serializers.DateField()
    quantity = serializers.IntegerField()
