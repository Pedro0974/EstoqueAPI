from rest_framework import generics, filters
from .serializers import SupplierSerializer
from .models import Supplier


class SupplierFilters(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        name = request.query_params.get('name', None)
        cnpj = request.query_params.get('cnpj', None)
        road = request.query_params.get('road', None)
        neighborhood = request.query_params.get('neighborhood', None)

        filters = {}

        if name:
            filters['name__icontains'] = name

        if cnpj:
            filters['cnpj'] = cnpj

        if road:
            filters['road__icontains'] = road

        if neighborhood:
            filters['neighborhood__icontains'] = neighborhood

        return queryset.filter(**filters)


class SupplierListCreateAPIView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = [SupplierFilters]


class SupplierRetrieveUpdateAPIVIew(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
