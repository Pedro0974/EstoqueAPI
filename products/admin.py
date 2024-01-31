from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'category',
        'quantity',
        'supplier'
    ]
    search_fields = [
        'name',
        'category',
        'supplier'
    ]