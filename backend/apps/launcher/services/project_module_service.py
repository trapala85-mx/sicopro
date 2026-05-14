import uuid

from django.db.models import QuerySet
from apps.launcher.models import Module

class ProjectModuleService:
    
    @staticmethod
    def get_project_modules(id:uuid, active: bool) -> QuerySet[Module]:
        
        if active:
            return ProjectModuleService._get_active_project_modules(id)
        
        return ProjectModuleService._get_all_project_modules(id)
    
    @staticmethod
    def _get_active_project_modules(id:uuid):
        return Module.objects.filter(is_active=True, projects__project_id=id)
    
    @staticmethod
    def _get_all_project_modules(id:uuid):
        return Module.objects.filter(projects__project_id=id)