from rest_framework.views import APIView
from apps.launcher.models import Project
from apps.launcher.serializers import ProjectOutputSerializer
from rest_framework import status
from apps.core.utils import str_to_bool
from apps.core.utils import success_response
from apps.launcher.enums import ProjectListViewEnums

class ProjectListview(APIView):

    def get(self, request):
        """
        1. Verificar si can_show viene
        """
        can_show = request.query_params.get('can_show', None)
        can_show = str_to_bool(can_show)

        """
        2. Hacmoes la búsqueda, si can_show es False que traiga todos si es True solo
        los activos. Esto es usando el modelo Project lo cual nos devolverá la queryset, 
        no los datos aún.
        """
        msg = ""
        if not can_show:
            projects = Project.objects.all()
            msg = ProjectListViewEnums.GET_ALL_PROJECTS
        else:
            projects = Project.objects.all().filter(is_active=True)
            msg = ProjectListViewEnums.GET_ALL_ACTIVE_PROJECTS

        """
        3. Necesitamos obtener los datos de manera correcta, para esto usamos el
        Serializer que nos devolverá serializer listo para cnvertir 1 o varios
        objetos. (para varios se debe incluir many=True)
        """
        serializer = ProjectOutputSerializer(instance=projects, many=True)

        """
        4. Obtener el diccionario de python limpio con el Serializer
        """
        projects_list = serializer.data
        
        return success_response(
            data= projects_list,
            msg=msg,
            status_code=status.HTTP_200_OK,
        )
