from django.urls import include, path

from .views import *

app_name = "course"


urlpatterns = [
	path('bulk-set-level/', BulkLevelSet.as_view(), name='bulk-set-level'),
    path('course/', course_list, name="course_list"),
    path('level/', level_list, name="level_list"),
]

