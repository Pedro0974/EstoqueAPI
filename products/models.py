from django.db import models
from core.models import DefaultInheritance
from categories.models import Category
from suppliers.models import Supplier


class Product(DefaultInheritance):
    name = models.CharField(
        'Name',
        max_length=255,
        blank=False,
        null=False
    )
    description = models.CharField(
        'Description',
        max_length=255,
        blank=False,
        null=False
    )
    image = models.ImageField(upload_to='media')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    min_quantity = models.IntegerField()
    max_quantity = models.IntegerField()
    quantity = models.IntegerField()
    price = models.DecimalField(
        'Price',
        decimal_places=2,
        max_digits=8
    )
    average_price = models.DecimalField(
        'Average Price',
        decimal_places=2,
        max_digits=8
    )

    class Meta:
        ordering = ('name', )
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name} - {self.price} - {self.description}'
