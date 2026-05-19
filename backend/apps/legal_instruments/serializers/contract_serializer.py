from rest_framework import serializers

from apps.core.utils import change_str_date
from apps.legal_instruments.models import Contract
from apps.legal_instruments.serializers.client_serializer import ClientOutputSerializer
from apps.legal_instruments.serializers.currency_serializer import CurrencyOutputSerializer


class ContractOutputSerializer(serializers.ModelSerializer):
    """Serializer para devolver los datos de una petición GET cuando el cliente solicita el
    contrato o el detalle de un contrato
    """

    clients = ClientOutputSerializer(many=True, read_only=True)
    currency = CurrencyOutputSerializer(read_only=True)
    sign_date = serializers.SerializerMethodField()
    expiration_date = serializers.SerializerMethodField()

    class Meta:
        model = Contract
        fields = [
            "id",
            "contract_number",
            "description",
            "sign_date",
            "expiration_date",
            "duration_days",
            "amount_before_tax",
            "amount_after_tax",
            "status",
            "project",
            "clients",
            "currency",
        ]

    def get_sign_date(self, obj):
        if obj.sign_date:
            return change_str_date(obj.sign_date)
        return ""

    def get_expiration_date(self, obj):
        if obj.expiration_date:
            return change_str_date(obj.expiration_date)
        return ""


class ContractWriteSerializer(serializers.ModelSerializer):
    """Serializer para los datos de Entrada para peticiones POST/PUT/PATCH cuando el usuario
    Crea o Edita un Contrato"""

    class Meta:
        model = Contract
        fields = [
            "id",
            "contract_number",
            "description",
            "sign_date",
            "expiration_date",
            "duration_days",
            "amount_before_tax",
            "amount_after_tax",
            "status",
            "project",
            "clients",
            "currency",
        ]


class ContractWriteOutputSerializer(serializers.ModelSerializer):
    """Serializer de la respuesta cuando se Crea / Edita un contrato"""

    class Meta:
        model = Contract
        fields = ["id", "contract_number"]
