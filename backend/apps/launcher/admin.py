from django.contrib import admin
from .models import Project, ProjectType, Module, ProjectTypeModule

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active","created_at", "updated_at",)
    search_fields = ("name","is_active")
    list_filter = ("name", )


@admin.register(ProjectType)
class ProjectTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at",)
    search_fields = ("name",)
    list_filter = ("name", )

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "parent", "order", "created_at", "updated_at",)
    search_fields = ('name', 'parent', 'order',)
    list_filter = ("name", 'parent', 'order',)

@admin.register(ProjectTypeModule)
class ProjectTypeModuleAdmin(admin.ModelAdmin):
    list_display = ("project_type", "module", "is_active", "created_at", "updated_at",)
    search_fields = ("project_type", "module")
    list_filter = ("project_type", "module")