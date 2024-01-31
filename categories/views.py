from rest_framework import generics, filters
from .models import Category
from .serializers import CategorySerializer


class CategoryFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        name = request.query_params.get('name', None)

        filters = {}

        if name:
            filters['name__icontains'] = name

        return queryset.filter(**filters)


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [CategoryFilter]


class CategoryRetrieveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
