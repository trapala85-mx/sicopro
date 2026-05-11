"""
Todas las excepciones que hereded de APIException son manejadas por DRF, igual Django's Http404 y PermissionDenied
DRF envía un response con status code y content-type.
Una función para un custom hanlder exception debe recibir 2 cosas:
    1. la excepcion que se manejará
    2. el diccionario que contiene el contexto o info de la excepción
Hay 3 tipos de errores:
    1. Los personalizados
    2. Los generales de DRF
    3. Los que nos manda el Serializer. En este caso sí tenemos "data" ya que nos da una lista de los campos y sus errores.
Por lo tanto, son 3 escenarios a verificar para que podamos enviar una respuesta bien estructurada.
"""
from rest_framework.views import exception_handler as drf_exception_handler
from apps.core.utils import error_response

def exception_handler(exc, context):
    msg = ""
    data = None
    # 1. llamar el default exception hanlder de DRF
    response = drf_exception_handler(exc, context)

    # 2. Verificar el mensaje de respuesta recibido
    if response is None:
        return None

    # 2.1. Menaje de nosotros:
    if hasattr(exc, 'message'):
        msg = exc.message
    # 2.2. Error general de DRF
    elif 'detail' in response.data:
        msg = response.data['detail']
    # 2.3. Error de validación Serializers.
    else:
        msg = "Error de validación."
        data = str(response.data)

    return error_response(
        success=success,
        msg=msg,
        status_code=response.status_code,
        data=data
        )