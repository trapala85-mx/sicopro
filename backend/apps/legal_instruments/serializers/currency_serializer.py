from rest_framework import serializers

from apps.core.models.currency import Currency


class CurrencyOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ["id", "code", "label"]
