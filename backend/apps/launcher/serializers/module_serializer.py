from rest_framework import serializers
from apps.launcher.models import Module

class ModuleOutputSerializer(serializers.ModelSerializer):

    submodules = serializers.SerializerMethodField()

    class Meta:
        model = Module
        fields = ['id', 'name', 'order', 'parent','is_active', 'submodules']
    
    def get_submodules(self, obj):
        submodules = obj.submodules.all()
        if submodules:
            return ModuleOutputSerializer(submodules, many=True).data
        return []