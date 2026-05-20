from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.legal_instruments.models.client import Client


class ClientListWithDataTests(APITestCase):
    def setUp(self):
        Client.objects.create(
            short_name="Tren Maya",
            business_name="Tren Maya, S.A. de C.V.",
            initials="TM",
        )
        Client.objects.create(
            short_name="ARTF",
            business_name="Agencia Reguladora de Transporte Ferroviario, S.A. de C.V.",
            initials="ARTF",
        )

    def test_get_all_clients_with_data(self):
        url = reverse("legal_instruments:client-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertEqual(len(response.data["data"]), 2)


class ClientListWithoutDataTests(APITestCase):
    def test_get_all_clients_without_data(self):
        url = reverse("legal_instruments:client-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertEqual(len(response.data["data"]), 0)
