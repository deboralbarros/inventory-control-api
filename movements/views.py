from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from products.models import Product
from .models import Movement
from .serializers import MovementSerializer, MovementSerializerOut


class ListCreateMovementView(APIView):
    def get(self, request):
        queryset = Movement.objects.all()
        serializer = MovementSerializerOut(queryset, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = MovementSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        data = serializer.data
        product = Product.objects.get(code=data.pop('product'))

        if (data['type'] == 'in'):
            product.stock_quantity = product.stock_quantity + data['quantity']

        elif (data['type'] == 'out'):
            if (product.stock_quantity > 0):
                product.stock_quantity = product.stock_quantity - \
                    data['quantity']

            else:
                return Response({'error': 'não pode'}, status.HTTP_400_BAD_REQUEST)

        product.save()

        movement = Movement.objects.create(**data, product=product)

        serializer = MovementSerializerOut(movement)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
