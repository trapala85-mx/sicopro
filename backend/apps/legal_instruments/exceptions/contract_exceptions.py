from rest_framework import status

from apps.core.exceptions import BaseException


class ContractStatusException(BaseException):
    def __init__(self, message):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, message=message)


class NoProjectInfoException(BaseException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Es necesario envíe dato del proyecto.",
        )


class NoContractFoundException(BaseException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            message="No se encontró el contrato.",
        )


class InvalidContractDataException(BaseException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Debe ingresar datos para el contrato.",
        )
