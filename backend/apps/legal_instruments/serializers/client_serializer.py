from rest_framework import serializers

from apps.legal_instruments.models.client import Client


class ClientOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "short_name", "business_name", "initials"]
