import uuid

from apps.legal_instruments.exceptions.contract_exceptions import (
    NoContractFoundException,
    NoProjectInfoException,
)
from apps.legal_instruments.models import Contract


class ContractService:
    @staticmethod
    def get_contract_by_project_id(project_id: uuid) -> Contract:

        # revisar si se envió el id del proyecto
        if not project_id:
            raise NoProjectInfoException()

        # buscamos el contrato en BD
        # retorna una instancia | None
        contract = Contract.objects.filter(project=project_id).first()

        # Verificar qué mensaje se debe enviar a la vista sobre el contrato
        msg = ContractService._msg_resp_when_getting_contract(contract)

        return contract, msg

    @staticmethod
    def get_contract_by_id(contract_id: uuid) -> Contract:

        contract = Contract.objects.filter(id=contract_id).first()

        if contract is None:
            raise NoContractFoundException()

        msg = ContractService._msg_resp_when_getting_contract(contract)

        return contract, msg

    @staticmethod
    def _msg_resp_when_getting_contract(contract: Contract) -> str:

        if contract is None:
            return "Aún no se ha creado contrato para este proyecto."

        return "Contrato obtenido correctamente."
