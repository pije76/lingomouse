from django.urls import path, re_path, include

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('courses', CourseViewSet, basename='course')
router.register('levels', LevelViewSet, basename='level')

urlpatterns = [
	path('', include(router.urls)),
]
