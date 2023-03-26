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
	# path('', include(router.urls)),
    # path('auth/', include('dj_rest_auth.urls')),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('google/', GoogleLogin.as_view(), name='google_login')

    # path("auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", include(router.urls)),
    # path("auth/", include("dj_rest_auth.urls")),
    # path("v1/auth/login/discord/", DiscordLogin.as_view(), name="discord_login"),
    # path("v1/auth/login/github/", GitHubLogin.as_view(), name="github_login"),
    # path("auth/login/google/", GoogleLogin.as_view(), name="google_login"),
    # path("v1/auth/registration/", include("dj_rest_auth.registration.urls")),
]

urlpatterns += [
    # path('auth/', include('rest_framework.urls')),
    path('auth/', include('dj_rest_auth.urls')),
#     path('auth/registration/', include('dj_rest_auth.registration.urls'))
    path("auth/google/", GoogleLogin.as_view(), name="google_login"),
]
