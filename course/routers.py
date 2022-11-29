from django.urls import path, re_path, include

from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *
from .api.views import CourseViewSet

# router = DefaultRouter(trailing_slash=True)
# router.register('courses', CourseViewSet, basename='courses')

urlpatterns = [
	# path('', include(router.urls)),
	# path('courses/', course_list, name="course_list"),
	# path('', include(router.urls)),
	# path('courses/', course_list, name="course_list"),
	re_path('', CourseViewSet.as_view({'get': 'list',}), name="course_list"),
	# re_path('', CourseViewSet.as_view({'get': 'retrieve', 'post': 'create', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name="course_list"),
	# path('courses/<int:pk>/', course_detail, name="course_detail"),
	# path('api/levels/', level_list, name="level_list"),
	# path('api/levels/<int:pk>/', level_detail, name="level_detail"),
	# path('api/words/', word_list, name="word_list"),
	# path('api/words/<int:pk>/', word_detail, name="word_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
