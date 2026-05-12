from apps.core.models import BaseModel
from django.db import models

class ProjectTypeModule(BaseModel):

    project_type = models.ForeignKey(
        to='ProjectType',
        on_delete=models.PROTECT,
        verbose_name="Tipo de proyecto",
        related_name="modules"
    )

    module = models.ForeignKey(
        to='Module',
        on_delete=models.PROTECT,
        verbose_name="Módulo",
        related_name="project_types"
    )
    is_active = models.BooleanField(default=True, verbose_name="Activo")

    @property
    def can_show(self) -> bool:
        return self.is_active and self.module.can_show