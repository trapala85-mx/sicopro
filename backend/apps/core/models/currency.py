from django.db import models

from .base_model import BaseModel


class Currency(BaseModel):
    code = models.CharField(max_length=3, unique=True)
    label = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.code.upper()
