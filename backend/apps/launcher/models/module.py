""" apps/launcer/models/module.ppy
Modelo para los módulos. Al tener un módulo submódulos se necesita una FK
hacia el mismo modelo. No queremos que se elimine nada si un módulo padre
teiene asignados submódulos.
"""
from apps.core.models import BaseModel
from django.db import models

class Module(BaseModel):

    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    parent = models.ForeignKey(
        to= 'self',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="submodules",
        verbose_name="Módulo padre"
    )
    order = models.IntegerField(verbose_name="Orden")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    
    @property
    def can_show(self) -> bool:
        """Shows if the module can be rendered or not.

        Returns:
            bool: True if can be showed in frontend , False if not.
        """
        return self.is_active


    def __str__(self):
        return self.name.capitalize()