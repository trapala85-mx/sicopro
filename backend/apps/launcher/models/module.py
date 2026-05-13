""" apps/launcer/models/module.ppy
Modelo para los módulos. Al tener un módulo submódulos se necesita una FK
hacia el mismo modelo. No queremos que se elimine nada si un módulo padre
teiene asignados submódulos.

Lógica del Guardado:

Module.save()
    ├── Guarda el módulo actual
    ├── Por cada hijo → hijo.save() (recursivo)
    │       └── Y ese hijo actualiza sus ProjectModule
    └── Actualiza todos sus ProjectModule de un golpe
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


    def save(self,*args, **kwargs):
        # Guardar el objeto que estamos trabajando
        super().save(*args, **kwargs)
        
        # Del objeto que estamos trabajando obtenemos submodules
        children = self.submodules.all()
        
        # De cada Module que es hijo, usamos esta misma función (recursividad)
        for child in children:
            child.is_active=self.is_active
            child.save()
        
        # Traer los ProjectModule del modulo que guardamos
        # En ProjectModule definimos que en Module veremos los ProjectModule con projects
        self.projects.update(is_active=self.is_active) 
        



    def __str__(self):
        return self.name.capitalize()