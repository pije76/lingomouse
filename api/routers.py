from django.urls import path, re_path, include

from rest_framework.routers import DefaultRouter
from rest_framework import routers

from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView

from .views import *

router = DefaultRouter()
router.register('courses', CourseViewSet, basename='course')
router.register('levels', LevelViewSet, basename='level')

urlpatterns = [
	path('', include(router.urls)),
    # path('auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
