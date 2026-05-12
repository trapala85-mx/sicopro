from django.contrib import admin
from .models import Project, ProjectType, Module

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