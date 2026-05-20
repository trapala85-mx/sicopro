from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.core.models.currency import Currency


class CurrencyListWithDataTests(APITestCase):
    def setUp(self):
        self.currency1 = Currency.objects.create(
            code="MXN",
            label="Peso Mexicano",
        )
        self.currency2 = Currency.objects.create(
            code="USD",
            label="Dolar Estadounidense",
        )

    def test_get_all_currencies_with_data(self):
        url = reverse("core:currencies-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertEqual(len(response.data["data"]), 2)


class CurrencyListWithoutDataTests(APITestCase):
    def test_get_all_clients_without_data(self):
        url = reverse("core:currencies-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertEqual(len(response.data["data"]), 0)
