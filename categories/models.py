from django.db import models
from core.models import DefaultInheritance


class Category(DefaultInheritance):
    name = models.CharField(
        'Name',
        max_length=100
    )

    class Meta:
        ordering = ('name', )
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'
