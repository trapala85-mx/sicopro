from django.urls import path

from apps.legal_instruments.views.client_list_view import ClientListView

from .views import ContractDetailView, ContractListView

app_name = "legal_instruments"

urlpatterns = [
    path("contracts/", view=ContractListView.as_view(), name="contract-list"),
    path("contracts/<uuid:id>/", view=ContractDetailView.as_view(), name="contract-detail"),
    path("clients/", view=ClientListView.as_view(), name="client-list"),
]
