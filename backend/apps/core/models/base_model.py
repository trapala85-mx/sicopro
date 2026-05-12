"""
apps/core/models/base_model.py

Clase base de todos lo modelos con atributos de auditoría por lo que debe ser abstracta para no generar tabla.

pk: uuid
created_at: datetime -> auto_now_add=True para que se genere solo cuando se cree.
updated_at: datetime -> auto_now=True para que se genere cada que se actualice.
"""

import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name="Fecha de creación",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name="Fecha de actualización",
    )

    class Meta:
        abstract = True
