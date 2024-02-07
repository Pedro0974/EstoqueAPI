from django.db import models
from core.models import DefaultInheritance
from products.models import Product
from suppliers.models import Supplier


class Prohibited(DefaultInheritance):
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField()
    price = models.DecimalField(
        'Price',
        max_digits=8,
        decimal_places=2
    )

    class Meta:
        ordering = ('date', )
        verbose_name = 'Prohibited'
        verbose_name_plural = 'Prohibiteds'

    def __str__(self):
        return f'{self.product} - {self.quantity} - {self.price}'


class Exit(DefaultInheritance):
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField()
    price = models.DecimalField(
        'Price',
        max_digits=8,
        decimal_places=2
    )

    class Meta:
        ordering = ('date', )
        verbose_name = 'Exit'
        verbose_name_plural = 'Exits'

    def __str__(self):
        return f'{self.product} - {self.quantity} - {self.price}'
