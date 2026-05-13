from apps.core.models import BaseModel
from django.db import models
from .project import Project
from .module import Module

class ProjectModule(BaseModel):

    project = models.ForeignKey(
        to=Project,
        on_delete=models.PROTECT,
        verbose_name="Proyecto",
        related_name="modules",
    )

    module = models.ForeignKey(
        to=Module,
        verbose_name="Proyectos del módulo",
        related_name="projects",
        on_delete=models.PROTECT,
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Activo"
    )

    