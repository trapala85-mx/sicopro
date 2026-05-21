from django.contrib import admin

from .models import Client, Contract, ContractClient


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "short_name",
        "business_name",
        "initials",
        "updated_at",
    )
    search_fields = (
        "short_name",
        "initials",
    )
    list_filter = (
        "short_name",
        "initials",
    )
    ordering = ("short_name",)


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = (
        "contract_number",
        "description",
        "sign_date",
        "expiration_date",
        "duration_days",
        "amount_before_tax",
        "amount_after_tax",
        "status",
        "currency",
    )
    search_fields = ("contract_number",)
    list_filter = ("contract_number", "status")
    ordering = ("contract_number",)


@admin.register(ContractClient)
class ContractClientAdmin(admin.ModelAdmin):
    list_display = (
        "contract",
        "client",
    )
    search_fields = ("contract__contract_number", "client__short_name")
    list_filter = ("contract", "client")
    ordering = ("contract", "client")
