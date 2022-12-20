from django.urls import include, path

from .views import *

app_name = "frontend"


urlpatterns = [
    path('', frontend, name="frontend"),
]

