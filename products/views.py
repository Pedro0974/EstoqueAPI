from rest_framework import generics, filters, status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from categories.models import Category
from suppliers.models import Supplier


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

    def perform_create(self, serializer):
        supplier_id = self.request.data.get('supplier')
        category_id = self.request.data.get('category')

        if not supplier_id:
            return Response(
                {"error": "Supplier ID is required"},
                status=status.HTTP_400_BAD_REQUEST)
        if not category_id:
            return Response(
                {"error": "Category ID is required"},
                status=status.HTTP_400_BAD_REQUEST)

        try:
            supplier = Supplier.objects.get(pk=supplier_id)
            category = Category.objects.get(pk=category_id)
        except Supplier.DoesNotExist:
            return Response(
                {"error": "Supplier not found"},
                status=status.HTTP_404_NOT_FOUND)
        except Category.DoesNotExist:
            return Response(
                {"error": "Category not found"},
                status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer.save(supplier=supplier, category=category)


class ProductRetrieveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
