from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import ProductSerializer
from .models import Products
from .filters import ProductFilter


class ListCreateProductView(ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter


class RetrieveUpdateDestroyProductView(RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
