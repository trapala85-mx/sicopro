from django.contrib import admin
from .models import Project, Module, ProjectModule

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active","created_at", "updated_at",)
    search_fields = ("name",)
    list_filter = ("name", )
    ordering = ('name',)

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "order", "is_active","created_at", "updated_at",)
    search_fields = ('name', 'parent',)
    list_filter = ("name", 'parent', 'order',)
    ordering = ("order",)

@admin.register(ProjectModule)
class ProjectModuleAdmin(admin.ModelAdmin):
    list_display = ('project', 'module','is_active', "created_at", "updated_at",)
    readonly_fields = ("project", "module", "is_active", "created_at", "updated_at")