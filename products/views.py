from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import ProductSerializer
from .models import Products


class ListCreateProductView(ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
