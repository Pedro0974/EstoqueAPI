from django.contrib import admin
from .models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'cnpj',
        'phone',
        'road',
        'house_number',
        'neighborhood',
        'email'
    ]
    search_fields = [
        'name',
        'cnpj',
        'phone',
        'road',
        'neighborhood'
    ]
