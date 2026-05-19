import uuid

from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView

from apps.core.utils import success_response
from apps.legal_instruments.serializers.contract_serializer import (
    ContractWriteOutputSerializer,
    ContractWriteSerializer,
)
from apps.legal_instruments.services import ContractService


class ContractDetailView(APIView):
    def put(self, request: Request, id: uuid):

        # 1. Traer el Contrato
        contract, msg = ContractService.get_contract_by_id(contract_id=id)

        # Serializar datos
        serializer = ContractWriteSerializer(instance=contract, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        output = ContractWriteOutputSerializer(instance=contract).data

        return success_response(
            msg=msg,
            status_code=status.HTTP_200_OK,
            data=output,
        )
