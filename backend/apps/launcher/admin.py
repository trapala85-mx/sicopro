from django.contrib import admin
from .models import Project, ProjectType

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