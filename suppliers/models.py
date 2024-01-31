from django.db import models
from core.models import DefaultInheritance


class Supplier(DefaultInheritance):
    name = models.CharField(
        'Name',
        max_length=255,
        blank=False,
        null=False
    )
    phone = models.CharField(
        'Phone Number',
        max_length=11,
        blank=False,
        null=False
    )
    cnpj = models.CharField(
        'CNPJ Number',
        max_length=15,
        blank=False,
        null=False
    )
    road = models.CharField(
        'Road Name',
        max_length=255,
        blank=False,
        null=False
    )
    neighborhood = models.CharField(
        'Neighborhood Name',
        max_length=255,
        blank=False,
        null=False
    )
    house_number = models.IntegerField(
        'House Number',
        blank=False,
        null=False
    )
    email = models.CharField(
        'Email',
        max_length=255,
        blank=False,
        null=False
    )

    class Meta:
        ordering = ('name', )
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return f'{self.name} - {self.cnpj}'
