from rest_framework import serializers
from apps.launcher.models import Project

class ProjectOutputSerializer(serializers.ModelSerializer):

    """Al ser una @property dbemos setear el valor con lógica y para
    esto usaremos el MethodField"""
    can_show = serializers.SerializerMethodField()

    class Meta:
        model = Project
        exclude = ['created_at', 'updated_at']
    
    def get_can_show(self, obj):
        """
        obj: instancia del modelo que está siendo serializado."""
        return obj.is_active