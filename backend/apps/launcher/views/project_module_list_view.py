import uuid

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework import status
from apps.core.utils import success_response
from apps.core.utils import str_to_bool
from apps.launcher.services import ProjectModuleService
from apps.launcher.serializers import ProjectModuleOutputSerializer
from apps.launcher.enums import ProjectModuleEnums

class ProjectModuleListView(APIView):

    def get(self, request:Request, id:uuid):

        is_active = str_to_bool(request.data.get('active', None))
        msg = ProjectModuleEnums.GET_ALL_ACTIVE_PROJECT_MODULES if is_active else ProjectModuleEnums.GET_ALL_PROJECT_MODULES
        
        project_modules = ProjectModuleService.get_project_modules(active=is_active, id=id)
        
        serializer = ProjectModuleOutputSerializer(project_modules, many=True)
        
        return success_response(
            data=serializer.data,
            msg=msg,
            status_code=status.HTTP_200_OK
        )