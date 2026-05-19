from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView

from apps.core.utils import str_to_bool, success_response
from apps.launcher.serializers import ModuleOutputSerializer
from apps.launcher.services import ModuleService


class ModuleListView(APIView):
    def get(self, request: Request):

        # 1. Obtener el active
        is_active = str_to_bool(value=request.query_params.get("active", None))

        # 2. Definir el mensaje a enviar
        # TODO: Pasarlo a un Enum
        msg = (
            "Se han extraido correctamente los módulos activos"
            if is_active
            else "Se han extraido correctamente todos los módulos registrados."
        )

        # Definir el tipo de búsqueda con base en 'is_active'
        modules = ModuleService.get_modules(active=is_active)

        # Serializar
        serializer = ModuleOutputSerializer(instance=modules, many=True)

        return success_response(
            data=serializer.data,
            status_code=status.HTTP_200_OK,
            msg=msg,
        )
