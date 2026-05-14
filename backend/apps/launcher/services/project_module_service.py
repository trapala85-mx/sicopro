import uuid

from django.db.models import QuerySet
from apps.launcher.models import ProjectModule

class ProjectModuleService:
    
    @staticmethod
    def get_project_modules(id:uuid, active: bool) -> QuerySet[ProjectModule]:
        
        if active:
            return ProjectModuleService._get_active_project_modules(id)
        
        return ProjectModuleService._get_all_project_modules(id)
    
    @staticmethod
    def _get_active_project_modules(id:uuid):
        return ProjectModule.objects.filter(is_active=True, project_id=id)
    
    @staticmethod
    def _get_all_project_modules(id:uuid):
        return ProjectModule.objects.filter(project_id=id)