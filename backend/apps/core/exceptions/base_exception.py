from rest_framework.exceptions import APIException

class BaseException(APIException):

    def __init__(self, status_code:int, message:str):
        super().__init__(detail=message)
        self.status_code = status_code
        self.message = message