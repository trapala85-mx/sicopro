from rest_framework import serializers
from apps.launcher.models import ProjectModule

class ProjectModuleOutputSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectModule
        fields = ['project', 'module', 'is_active']