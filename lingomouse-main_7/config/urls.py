from django.urls import path
from .views import SetupThemeMode

app_name = 'config'

urlpatterns = [
	path('setup-theme-mode/', SetupThemeMode.as_view(), name='setup-theme-mode'),
]
