from django.urls import path

from .views import *

app_name = 'config'

urlpatterns = [
	path('setup-theme-mode/', SetupThemeMode.as_view(), name='setup-theme-mode'),

    path('', config_index, name="config_index"),

    path('country/', country_list, name="country_list"),
    path('language/', language_list, name="language_list"),
]
