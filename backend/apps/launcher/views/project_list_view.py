from rest_framework import status
from rest_framework.views import APIView

from apps.core.utils import str_to_bool, success_response
from apps.launcher.enums import ProjectEnums
from apps.launcher.serializers import ProjectOutputSerializer
from apps.launcher.services import ProjectService


class ProjectListview(APIView):
    def get(self, request):
        """
        1. Verificar si is_active viene.
        """
        is_active = str_to_bool(request.query_params.get("active", None))
        msg = ProjectEnums.GET_ALL_ACTIVE_PROJECTS if is_active else ProjectEnums.GET_ALL_PROJECTS

        """
        2. Delegamos al Service la lógica para obtener los Queryset.
        """
        projects = ProjectService.get_projects(active=is_active)
        """
        4. Obtener el diccionario de python limpio con el Serializer
        """
        serializer = ProjectOutputSerializer(instance=projects, many=True)
        projects_list = serializer.data

        return success_response(
            data=projects_list,
            msg=msg,
            status_code=status.HTTP_200_OK,
        )
