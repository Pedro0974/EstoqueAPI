import uuid
from django.db import models

# Create your models here.


class UuidModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        editable=False,
        default=uuid.uuid4
    )

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    created_in = models.DateTimeField(
        'Created in',
        auto_now_add=True
    )
    modified_in = models.DateTimeField(
        'Modified in',
        auto_now=True
    )

    class Meta:
        abstract = True


class Active(models.Model):
    ativo = models.BooleanField(
        'Active?',
        default=True
    )

    class Meta:
        abstract = True


class DefaultInheritance(UuidModel, TimeStampedModel, Active):
    class Meta:
        abstract = True
