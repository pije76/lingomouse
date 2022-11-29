from django.urls import include, path

from .views import *
from . import views

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "course"


urlpatterns = [
	path('bulk-set-level/', BulkLevelSet.as_view(), name='bulk-set-level'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
