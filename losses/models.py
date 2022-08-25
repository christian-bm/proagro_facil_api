import uuid

from django.db import models


class EventTypeChoices(models.TextChoices):
    CHUVA = "chuva excessiva"
    GEADA = "geada"
    GRANIZO = "granizo"
    SECA = "seca"
    VENDAVAL = "vendaval"
    RAIO = "raio"
    OUTRO = "outro"


class Loss(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    first_name = models.CharField(max_length=125, null=False)
    last_name = models.CharField(max_length=125, null=False)
    email = models.EmailField(max_length=255, null=False)
    cpf = models.CharField(max_length=11, null=False)
    latitude = models.CharField(max_length=14, null=False)
    longitude = models.CharField(max_length=14, null=False)
    farming_type = models.CharField(max_length=125, null=False)
    harvest_date = models.DateField()
    event_type = models.CharField(
        max_length=20, choices=EventTypeChoices.choices, default=EventTypeChoices.OUTRO
    )
