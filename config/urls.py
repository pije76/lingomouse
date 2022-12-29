from django.urls import path

from .views import *

app_name = 'config'

urlpatterns = [
	path('setup-theme-mode/', setup_theme_mode, name='setup_theme_mode'),

    path('', config_index, name="config_index"),

    path('country/', country_list, name="country_list"),
    path('language/', language_list, name="language_list"),

    path('country/<int:pk>/detail/', country_detail, name='country_detail'),
    path('language/<int:pk>/detail/', language_detail, name='language_detail'),

    path('country/add/', country_add, name='country_add'),
    path('language/add/', language_add, name='language_add'),
]
