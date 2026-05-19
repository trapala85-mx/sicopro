import uuid

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.core.models import Currency
from apps.launcher.models import Project
from apps.legal_instruments.models import Contract
from apps.legal_instruments.models.client import Client


class ContractListTests(APITestCase):
    def setUp(self):
        self.proyecto_1 = Project.objects.create(
            name="Supervisión Tren Maya Tramo 2",
            is_active=True,
        )
        self.proyecto_2 = Project.objects.create(
            name="Supervisión Tren Maya Tramo 3",
            is_active=True,
        )
        self.cliente_1 = Client.objects.create(
            short_name="Tren Maya",
            business_name="Tren Maya, S.A. de C.V.",
            initials="TM",
        )
        self.currency1 = Currency.objects.create(
            code="MXN",
            label="Peso Mexicano",
        )
        self.contrato_1 = Contract.objects.create(
            contract_number="TM-001",
            description="Supervisión de la construcción del Tren Maya Tramo 2.",
            sign_date="2024-01-15",
            expiration_date="2025-01-15",
            duration_days=365,
            amount_before_tax=0,
            amount_after_tax=0,
            status=Contract.Status.ACTIVE,
            currency=self.currency1,
            project=self.proyecto_1,
        )
        self.contrato_1.clients.add(self.cliente_1)

    def test_get_contract_for_project_ok(self):
        url = reverse("legal_instruments:contract-list")
        response = self.client.get(url, data={"project": self.proyecto_1.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["success"], True)
        self.assertEqual(len(response.data), 4)

    def test_get_contract_for_project_error(self):
        url = reverse("legal_instruments:contract-list")
        response = self.client.get(url, data={"project": ""})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["success"], False)
        self.assertEqual(response.data["data"], None)

    def test_get_none_contract_for_project_ok(self):
        url = reverse("legal_instruments:contract-list")
        response = self.client.get(url, data={"project": self.proyecto_2.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["success"], True)
        self.assertEqual(response.data["data"], None)

    def test_post_create_contract_ok(self):
        url = reverse("legal_instruments:contract-list")
        self.data = {
            "contract_number": "TM-002",
            "description": "Supervisión de la construcción del Tren Maya Tramo 3.",
            "sign_date": "2024-01-15",
            "expiration_date": "2025-01-15",
            "duration_days": 365,
            "amount_before_tax": 0,
            "amount_after_tax": 0,
            "status": Contract.Status.ACTIVE,
            "currency": self.currency1.id,
            "project": self.proyecto_2.id,
            "clients": [self.cliente_1.id],
        }
        response = self.client.post(
            url,
            data=self.data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["success"], True)

    def test_post_create_contract_error(self):
        url = reverse("legal_instruments:contract-list")
        self.data = {}
        response = self.client.post(
            url,
            data=self.data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["success"], False)
        self.assertIsNotNone(response.data["data"])

    def test_put_edit_contract_ok(self):
        url = reverse("legal_instruments:contract-detail", kwargs={"id": self.contrato_1.id})
        self.data = {
            "contract_number": "TM-003",
            "description": "Supervisión de la construcción del Tren Maya Tramo 3.",
            "sign_date": "2024-01-15",
            "expiration_date": "2025-01-15",
            "duration_days": 365,
            "amount_before_tax": 0,
            "amount_after_tax": 0,
            "status": Contract.Status.ACTIVE,
            "currency": self.currency1.id,
            "project": self.proyecto_2.id,
            "clients": [self.cliente_1.id],
        }

        response = self.client.put(
            url,
            data=self.data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["success"], True)
        self.assertEqual(response.data["data"]["contract_number"], "TM-003")

    def test_contract_not_found(self):
        url = reverse("legal_instruments:contract-detail", kwargs={"id": uuid.uuid4()})
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["success"], False)
        self.assertEqual(response.data["data"], None)
