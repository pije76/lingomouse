from django.urls import path

from .views import *

app_name = 'config'

urlpatterns = [
	path('setup-theme-mode/', SetupThemeMode.as_view(), name='setup-theme-mode'),
    path('', config_set, name="config_set"),
]
