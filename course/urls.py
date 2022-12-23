from django.urls import include, path

from .views import *

app_name = "course"


urlpatterns = [
	path('bulk-set-level/', BulkLevelSet.as_view(), name='bulk-set-level'),
    path('', course_index, name="course_index"),
    path('course/', course_list, name="course_list"),
    path('level/', level_list, name="level_list"),
    path('word/', word_list, name="word_list"),

    path('<int:pk>', change_course, name='change_course'),
    path('<int:pk>', change_level, name='change_level'),
]

