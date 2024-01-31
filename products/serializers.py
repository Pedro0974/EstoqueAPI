from rest_framework import serializers
from .models import Product
from categories.serializers import CategorySerializer
from suppliers.serializers import SupplierSerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    supplier = SupplierSerializer()

    class Meta:
        model = Product
        fields = '__all__'
