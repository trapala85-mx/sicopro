from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView

from apps.core.models import Currency
from apps.core.serializes import CurrencyOutputSerializer
from apps.core.utils import success_response


class CurrencyListView(APIView):
    def get(self, request: Request):
        """Retorna todos las monedas registradas."""

        # 1. Obtener Monedas/currencies del Service
        currencies = Currency.objects.all()

        # 2. Pasarlos al Serializer
        data = CurrencyOutputSerializer(instance=currencies, many=True).data

        # 3. Mensaje
        msg = "Monedas obtenidas." if len(data) > 0 else "No hay monedas registradas."

        return success_response(
            status_code=status.HTTP_200_OK,
            msg=msg,
            data=data,
        )
