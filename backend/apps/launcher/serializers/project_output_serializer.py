from rest_framework import serializers
from apps.launcher.models import Project

class ProjectOutputSerializer(serializers.ModelSerializer):

    """Al ser una @property dbemos setear el valor con lógica y para
    esto usaremos el MethodField"""

    class Meta:
        model = Project
        exclude = ['created_at', 'updated_at']
    