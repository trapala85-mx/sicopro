from django.contrib import admin

from .models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("label", "code")
    search_fields = ("code",)
    ordering = ("code",)
    list_filter = ("label", "code")
