from rest_framework import generics, filters, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import Prohibited, Exit
from .serializers import (
    ProhibitedSerializer,
    ExitSerializer
)


class ProhibitedFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        name = request.query_params.get('name', None)
        price = request.query_params.get('price', None)
        quantity = request.query_params.get('quantity', None)
        date = request.query_params.get('date', None)

        filters = {}

        if name:
            filters['name__icontains'] = name

        if price:
            filters['price'] = price

        if quantity:
            filters['quantity'] = quantity

        if date:
            filters['date'] = date

        return queryset.filter(**filters)


class ProhibitedListCreateAPIView(generics.ListCreateAPIView):
    queryset = Prohibited.objects.all()
    serializer_class = ProhibitedSerializer
    filter_backends = [ProhibitedFilter]

    def perform_create(self, serializer):
        data = serializer.validated_data

        try:
            product = data['product']
            quantity = data['quantity']
            price = data['price']

            self.update_product_quantity(product, quantity)
            self.calculate_average_price(product, quantity, price)

            serializer.save()
        except KeyError as e:
            raise ValidationError({"error": f"Missing key: {e}"})

    def update_product_quantity(self, product, quantity):
        product.quantity += quantity
        product.save()

    def calculate_average_price(self, product, quantity, price):
        total_price = product.average_price * product.quantity
        total_price += quantity * price
        product.quantity += quantity

        if product.quantity != 0:
            product.average_price = total_price / product.quantity
        else:
            product.average_price = 0
        product.save()


class ProhibitedRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Prohibited.objects.all()
    serializer_class = ProhibitedSerializer


class ExitFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        name = request.query_params.get('name', None)
        price = request.query_params.get('price', None)
        quantity = request.query_params.get('quantity', None)
        date = request.query_params.get('date', None)

        filters = {}

        if name:
            filters['name__icontains'] = name

        if price:
            filters['price'] = price

        if quantity:
            filters['quantity'] = quantity

        if date:
            filters['date'] = date

        return queryset.filter(**filters)


class ExitListCreateAPIView(generics.ListCreateAPIView):
    queryset = Exit.objects.all()
    serializer_class = ExitSerializer
    filter_backends = [ExitFilter]

    def perform_create(self, serializer):
        data = serializer.validated_data

        try:
            product = data['product']
            quantity = data['quantity']
            price = data['price']

            self.update_product_quantity(product, quantity)
            self.calculate_average_price(product, quantity, price)

            serializer.save()
        except KeyError as e:
            raise ValidationError({"error": f"Missing key: {e}"})

    def update_product_quantity(self, product, quantity):
        product.quantity -= quantity
        product.save()

    def calculate_average_price(self, product, quantity, price):
        total_price = product.average_price * product.quantity
        total_price -= quantity * price
        product.quantity -= quantity

        if product.quantity != 0:
            product.average_price = total_price / product.quantity
        else:
            product.average_price = 0
        product.save()


class ExitRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Exit.objects.all()
    serializer_class = ExitSerializer
