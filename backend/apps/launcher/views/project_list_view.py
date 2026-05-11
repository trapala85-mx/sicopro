from rest_framework.views import APIView
from apps.launcher.serializers import ProjectOutputSerializer
from rest_framework import status
from apps.core.utils import str_to_bool
from apps.core.utils import success_response
from apps.launcher.enums import ProjectListViewEnums
from apps.launcher.services import ProjectService
class ProjectListview(APIView):

    def get(self, request):
        """
        1. Verificar si can_show viene.
        """
        can_show = str_to_bool(request.query_params.get('can_show', None))
        msg = ProjectListViewEnums.GET_ALL_ACTIVE_PROJECTS if can_show else ProjectListViewEnums.GET_ALL_PROJECTS
        
        """
        2. Delegamos al Service la lógica para obtener los Queryset.
        """
        projects = ProjectService.get_projects(can_show=can_show)
        """
        4. Obtener el diccionario de python limpio con el Serializer
        """
        serializer = ProjectOutputSerializer(instance=projects, many=True)
        projects_list = serializer.data
        
        return success_response(
            data= projects_list,
            msg=msg,
            status_code=status.HTTP_200_OK,
        )
