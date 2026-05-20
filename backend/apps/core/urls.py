from django.urls import path

from apps.core.views import CurrencyListView

app_name = "core"

urlpatterns = [
    path("currencies/", view=CurrencyListView.as_view(), name="currencies-list"),
]
