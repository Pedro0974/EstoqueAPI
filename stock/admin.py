from django.contrib import admin
from .models import Prohibited, Exit


@admin.register(Prohibited)
class ProhibitedAdmin(admin.ModelAdmin):
    list_display = [
        'date',
        'product',
        'supplier',
        'quantity',
        'price'
    ]
    search_fields = [
        'date',
        'product',
        'supplier'
    ]


@admin.register(Exit)
class ExitAdmin(admin.ModelAdmin):
    list_display = [
        'date',
        'product',
        'quantity',
        'price'
    ]
    search_fields = [
        'date',
        'product'
    ]
