from rest_framework import serializers

from apps.core.utils import change_str_date
from apps.legal_instruments.models import Contract
from apps.legal_instruments.serializers.client_serializer import (
    ClientOutputSerializer,
)
from apps.legal_instruments.serializers.currency_serializer import (
    CurrencyOutputSerializer,
)


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

    clients = ClientOutputSerializer(many=True)

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

    def create(self, validated_data):
        # sacamos el atributo de los datos validados para no pasarlo al create
        clients_list = validated_data.pop("clients")  # lista de objetos Client
        # creatmos el objeto contracto sin clients
        contract = Contract.objects.create(**validated_data)
        # como contract.clients es una lista, se usa set para enviar la lista de clientes
        contract.clients.set(clients_list)
        return contract

    def update(self, instance: Contract, validated_data):
        # extraer datos de clientes
        clients_list = validated_data.pop("clients")
        # actualizar campos de validates_Data
        for key, value in validated_data.items():
            setattr(instance, key, value)
        # guardamos la instancia sin clientes
        instance.save()
        # seteamos los clientes
        instance.clients.set(clients_list)

        return instance


class ContractWriteOutputSerializer(serializers.ModelSerializer):
    """Serializer de la respuesta cuando se Crea / Edita un contrato"""

    class Meta:
        model = Contract
        fields = ["id", "contract_number"]
