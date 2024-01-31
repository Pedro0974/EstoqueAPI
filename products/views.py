from rest_framework import generics, filters
from .models import Product
from .serializers import ProductSerializer


class ProductFilters(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        name = request.query_params.get('name', None)
        price = request.query_params.get('price', None)
        quantity = request.query_params.get('quantity', None)
        min_quantity = request.query_params.get('min_quantity', None)
        max_quantity = request.query_params.get('max_quantity', None)

        filters = {}

        if name:
            filters['name__icontains'] = name

        if price:
            filters['price'] = price

        if quantity:
            filters['quantity'] = quantity

        if min_quantity:
            filters['min_quantity'] = min_quantity

        if max_quantity:
            filters['max_quantity'] = max_quantity

        return queryset.filter(**filters)


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [ProductFilters]


class ProductRetrieveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
