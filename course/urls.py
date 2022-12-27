from django.urls import include, path

from .views import *

app_name = "course"


urlpatterns = [
	path('bulk-set-level/', BulkLevelSet.as_view(), name='bulk-set-level'),

    path('', course_index, name="course_index"),
    path('course/', course_list, name="course_list"),
    path('level/', level_list, name="level_list"),
    path('word/', word_list, name="word_list"),

    path('course/<int:pk>/detail/', course_detail, name='course_detail'),
    path('level/<int:pk>/detail/', level_detail, name='level_detail'),
    path('word/<int:pk>/detail/', word_detail, name='word_detail'),

    path('course/add/', course_add, name='course_add'),
    path('level/add/', level_add, name='level_add'),
    path('word/add/', word_add, name='word_add'),

]

