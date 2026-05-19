from django.db import models

from apps.core.models import BaseModel


class ContractClient(BaseModel):
    contract = models.ForeignKey(
        to="Contract",
        on_delete=models.PROTECT,
        related_name="client_links",
    )

    client = models.ForeignKey(
        to="Client",
        on_delete=models.PROTECT,
        related_name="contract_links",
    )
    # EL related_name en este modelo lo usaríamos solo cuando necestiemos
    # acceder a la tabla pivote irectamente (ContractClient) para cuando
    # agreguemos datos a esta tabla.
