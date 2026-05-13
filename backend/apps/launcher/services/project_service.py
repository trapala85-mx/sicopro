from django.db.models import QuerySet
from apps.launcher.models import Project


class ProjectService:

    @staticmethod
    def get_projects(active:bool) -> QuerySet[Project]:
        """Retorna la Queryset para obtener todos los proyectos o solo los activos en sistema.
        
        params:
            active: bool. True muestra solo los activos, False todos los del sistema."""
        if active:
            return ProjectService._get_all_active_projects()
        
        return ProjectService._get_all_projects()


    @staticmethod
    def _get_all_projects() -> QuerySet[Project]:
        """Crea la Queryset para obtener todos los proyectos en el sistema."""
        
        return Project.objects.all()
    
    @staticmethod
    def _get_all_active_projects() -> QuerySet[Project]:
        """Crea la Queryset para obtener todos los proyectos activos en el sistema."""

        return Project.objects.filter(is_active=True)