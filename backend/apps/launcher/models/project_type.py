"""
apps/launcher/models/peroject_type.py

Modelo para el Tipo de Proyecto, no puede haber dos tipos de proyectos con el mismo nombre.
name : str & unique
"""

from apps.core.models import BaseModel
from django.db import models


class ProjectType(BaseModel):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nombre")

    def __str__(self):
        return self.name.capitalize()
