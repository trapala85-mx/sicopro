from django.db import models

from apps.core.models import BaseModel


class Client(BaseModel):
    short_name = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    business_name = models.CharField(max_length=255, verbose_name="Razón social")
    initials = models.CharField(max_length=10, verbose_name="Siglas")

    def __str__(self) -> str:
        return self.short_name.capitalize()
