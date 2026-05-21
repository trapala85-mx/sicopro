"""Modelo de Contrato
NOTA: Migración a microservicio.
@param project: Proyecto asociado al contrato
Este vive en otra app que al migrar a microservicio se vovlerá un UUIDField no FK
Como se crea una BD por aplicación, se necesitará manejo por eventos como puede ser que al
crearse un Proyecto gener un evento project_created que será escuchado por Contract para traer el
UUID del proyecto y asociarlo o incluso traer toda la info del Proyecto de ser necesario.
"""

from django.db import models

from apps.core.models import BaseModel, Currency


class Contract(BaseModel):
    class Status(models.TextChoices):
        ACTIVE = "active", "Activo"
        CANCELLED = "cancelled", "Cancelado"
        COMPLETED = "completed", "Terminado"

    contract_number = models.CharField(max_length=100, unique=True, verbose_name="Número")
    description = models.TextField(verbose_name="Objeto de contrato")
    sign_date = models.DateField(verbose_name="Fecha de firma")
    expiration_date = models.DateField(verbose_name="Fecha de fin")
    duration_days = models.IntegerField(verbose_name="Duración")
    amount_before_tax = models.DecimalField(
        max_digits=17,
        decimal_places=2,
        verbose_name="Importe sin IVA",
    )
    amount_after_tax = models.DecimalField(
        max_digits=17,
        decimal_places=2,
        verbose_name="Importe con IVA",
    )
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE, verbose_name="Estado")
    clients = models.ManyToManyField(
        to="Client",
        related_name="contracts",
        verbose_name="Clientes",
        through="ContractClient",
    )
    currency = models.ForeignKey(
        to=Currency,
        on_delete=models.PROTECT,
        related_name="contracts",
        verbose_name="Moneda",
    )

    project = models.OneToOneField(
        to="launcher.Project",
        on_delete=models.PROTECT,
        related_name="contract",
        verbose_name="Proyecto",
    )

    def __str__(self):
        return f"{self.contract_number}"
