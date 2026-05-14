from apps.launcher.models import Module
from django.db.models import QuerySet

class ModuleService:

    @staticmethod
    def get_modules(active:bool) -> QuerySet[Module]:
        """Retorna el QuerySet que hace la búsqueda de todos los módulos
        
        params:
            active: bool. True trae"""
        if active:
            return ModuleService._get_all_active_modules()
        
        return ModuleService._get_all_modules()

    @staticmethod
    def _get_all_active_modules() -> QuerySet[Module]:
        """Crea la QuerySet para obtener todos los modulos activos."""
        
        return Module.objects.filter(is_active=True)

    @staticmethod
    def _get_all_modules() -> QuerySet[Module]:
        """Crea la QuerySet para obtener todos los módulos activos"""

        return Module.objects.all()