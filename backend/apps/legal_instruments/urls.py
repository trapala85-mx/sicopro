from django.urls import path

from .views import ContractDetailView, ContractListView

app_name = "legal_instruments"

urlpatterns = [
    path("", view=ContractListView.as_view(), name="contract-list"),
    path("<uuid:id>/", view=ContractDetailView.as_view(), name="contract-detail"),
]
