from django_filters import rest_framework as filters

from .models import Products, PRODUCT_TYPE_CHOICES


class ProductFilter(filters.FilterSet):
    type = filters.ChoiceFilter(choices=PRODUCT_TYPE_CHOICES)
    description = filters.CharFilter(
        field_name='description', lookup_expr='icontains')

    class Meta:
        model = Products
        fields = ['type', 'description']
