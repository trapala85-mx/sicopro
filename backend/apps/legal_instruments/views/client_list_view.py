from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView

from apps.core.utils import success_response
from apps.legal_instruments.models import Client
from apps.legal_instruments.serializers.client_serializer import ClientOutputSerializer


class ClientListView(APIView):
    def get(self, request: Request):
        """Retorna todos los clientes registrados."""

        # 1. Obtener Clientes del Service
        clients = Client.objects.all()

        # 2. Pasarlos al Serializer
        data = ClientOutputSerializer(instance=clients, many=True).data

        # 3. Mensaje
        msg = "Clientes obtenidos." if len(data) > 0 else "No hay clientes registrados."

        return success_response(
            status_code=status.HTTP_200_OK,
            msg=msg,
            data=data,
        )
