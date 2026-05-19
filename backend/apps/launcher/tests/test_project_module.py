from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.launcher.models import Module, Project, ProjectModule


class ProjectModuleTest(APITestCase):
    def setUp(self):
        self.proyecto_1 = Project.objects.create(
            name="Tren QI",
            is_active=True,
        )
        self.modulo_home = Module.objects.create(
            name="Home",
            order=0,
        )
        self.modulo_instrumentos = Module.objects.create(
            name="Instrumentos Legales",
            order=100,
        )
        self.modulo_contrato = Module.objects.create(
            name="Contrato", order=110, parent=self.modulo_instrumentos
        )
        self.proyecto1_home = ProjectModule.objects.create(
            project=self.proyecto_1,
            module=self.modulo_home,
        )
        self.proyecto_1_instrumentos = ProjectModule.objects.create(
            project=self.proyecto_1,
            module=self.modulo_instrumentos,
        )

    def test_get_project_modules(self):
        url = reverse("launcher:list-modules-for-project", kwargs={"id": self.proyecto_1.id})

        response = self.client.get(url, data={"active": True})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["data"]), 2)
