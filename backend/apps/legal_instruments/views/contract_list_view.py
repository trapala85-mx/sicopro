from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView

from apps.core.utils import success_response
from apps.legal_instruments.serializers.contract_serializer import (
    ContractOutputSerializer,
    ContractWriteOutputSerializer,
    ContractWriteSerializer,
)
from apps.legal_instruments.services import ContractService


class ContractListView(APIView):
    def get(self, request: Request):
        """Maneja peticiones GET para traer el ccontrato de un proyecto en específico.

        query_params:
            project: uuid. id del proyecto.
        """

        # Obtener el project_id de los query_params
        project_id = request.query_params.get("project", "")

        # Servicio con lógica para retornar instancia o elever error.
        contract, msg = ContractService.get_contract_by_project_id(project_id=project_id)

        data = None
        if contract is not None:
            data = ContractOutputSerializer(instance=contract).data
            msg = "Contrato obtenido correctamente."

        return success_response(
            status_code=status.HTTP_200_OK,
            msg=msg,
            data=data,
        )

    def post(self, request: Request):
        """Mètodo POST para crear un nuevo Contract.

        params:
            request.data: dict|QueryDict. Diccionario con los datos del body.
        """
        # 1. Crear el serializer que verificará los datos
        serializer = ContractWriteSerializer(data=request.data)

        # 2. Validar los datos diciéndo que eleve exception
        serializer.is_valid(raise_exception=True)

        # 3. Si están bien los datos, crear los datos en la base de datos
        contract = serializer.save()

        # 4. pasar los datos por el serializador de salida
        output = ContractWriteOutputSerializer(instance=contract)

        return success_response(
            data=output.data,
            msg="Contrato creado correctamente.",
            status_code=status.HTTP_201_CREATED,
        )
