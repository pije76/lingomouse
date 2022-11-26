from django.urls import path
from .views import BulkLevelSet

app_name = "course"
urlpatterns = [
	path('bulk-set-level/', BulkLevelSet.as_view(), name='bulk-set-level'),
]
