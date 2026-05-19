"""
apps/launcher/models/project.py

Modelo para el Proyecto, no puede haber dos Proyectos con el mismo nombre.
Tiene un FK con el modelo ProjectType donde usaremos como related_name projects
para que en ProjectType aparezta projects la relación con muchos Proyectos.
"""

from django.db import models

from apps.core.models import BaseModel


class Project(BaseModel):
    name = models.CharField(max_length=200, unique=True, verbose_name="Nombre")
    is_active = models.BooleanField(default=True, verbose_name="Activo")

    def __str__(self) -> str:
        """Return Name of the Project.

        Returns:
            str: Name of the project.
        """
        return self.name.capitalize()
