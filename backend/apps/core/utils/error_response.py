from rest_framework.response import Response

def error_response(data: dict, msg:str, status_code:int, success:bool = False):

    resp = {
        "success": success,
        "msg": msg,
        "status_code": status_code,
        "data": data
    }

    return Response(data=resp, status=status_code)