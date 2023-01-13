from django.urls import include, path

from .views import *

app_name = "course"


urlpatterns = [
	path('bulk-set-level/', BulkLevelSet.as_view(), name='bulk-set-level'),

    path('', course_list, name="course_list"),
    # path('course/', course_list, name="course_list"),
    path('course/add/', course_add, name='course_add'),
    path('course/<int:pk>/detail/', course_detail, name='course_detail'),
    path('course/<int:pk>/delete/', course_delete, name='course_delete'),

    path('level/', level_list, name="level_list"),
    path('level/add/', level_add, name='level_add'),
    path('level/<int:pk>/detail/', level_detail, name='level_detail'),
    path('level/<int:pk>/delete/', level_delete, name='level_delete'),

    path('word/', word_list, name="word_list"),
    path('word/add/', word_add, name='word_add'),
    path('word/<int:pk>/detail/', word_detail, name='word_detail'),
    path('word/<int:pk>/delete/', word_delete, name='word_delete'),
    path('word/export/', word_export, name='word_export'),
    path('word/import/', word_import, name='word_import'),

]

