from django.urls import include, path

from .views import *

app_name = "homepage"


urlpatterns = [
    path('', homepage, name="homepage"),
]

