from rest_framework.serializers import ModelSerializer

from apps.core.models import Currency


class CurrencyOutputSerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = ["id", "label", "code"]
