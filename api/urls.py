from django.urls import path, re_path, include

from rest_framework import routers

from .views import CourseViewSet, LevelViewSet

app_name = "api"

router = routers.DefaultRouter(trailing_slash=True)
router.register('courses', CourseViewSet)
router.register('levels', LevelViewSet)

urlpatterns = router.urls

# urlpatterns = [
    # path('', include(router.urls)),
#     re_path('', CourseViewSet.as_view({'get': 'list',}), name="course_list"),
#     re_path('', LevelViewSet.as_view({'get': 'list',}), name="level_list"),
# ]
