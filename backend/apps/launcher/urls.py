from django.urls import path
from .views import ProjectListview, ModuleListView

app_name = 'launcher'

urlpatterns = [
    path('projects/', view=ProjectListview.as_view(), name='list-projects'),
    path('modules/', view=ModuleListView.as_view(), name='list-modules'),
]