from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("apps.launcher.urls")),
    path("api/v1/contracts/", include("apps.legal_instruments.urls")),
]
