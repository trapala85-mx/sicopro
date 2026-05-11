"""
apps/launcher/models/project.py

Modelo para el Proyecto, no puede haber dos Proyectos con el mismo nombre.
Tiene un FK con el modelo ProjectType donde usaremos como related_name projects
para que en ProjectType aparezta projects la relación con muchos Proyectos.
"""

from apps.core.models import BaseModel
from django.db import models


class Project(BaseModel):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nombre")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    project_type = models.ForeignKey(
        to="launcher.ProjectType",
        on_delete=models.PROTECT,
        related_name="projects",
        verbose_name="Tipo de Proyecto",
    )

    @property
    def can_show(self) -> bool:
        """Shows if the project can be redered or not.

        Returns:
            bool: True if can be showed in frontend , False if not.
        """
        return self.is_active

    def __str__(self) -> str:
        """Return Name of the Project.

        Returns:
            str: Name of the project.
        """
        return self.name.capitalize()
