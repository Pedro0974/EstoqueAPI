from rest_framework import serializers
from .models import Prohibited, Exit
from products.serializers import ProductSerializer
from suppliers.serializers import SupplierSerializer


class ProhibitedSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    supplier = SupplierSerializer()

    class Meta:
        model = Prohibited
        fields = '__all__'


class ExitSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    supplier = SupplierSerializer()

    class Meta:
        model = Exit
        fields = '__all__'
