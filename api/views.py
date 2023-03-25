from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import transaction
from django.forms.models import model_to_dict
from django.http import Http404, HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.encoding import smart_str
from django.utils.translation import gettext_lazy as _
from django.views import View

# from rest_framework import generics, permissions, renderers, viewsets, status, mixins, pagination, permissions, renderers, viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from course.models import *
from course.serializers import *

from .paginations import *


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all().order_by('id')
    serializer_class = CourseSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)


class LevelViewSet(ModelViewSet):
    queryset = Level.objects.all().order_by('id')
    serializer_class = LevelSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        queryset = Level.objects.all()
        serializer = LevelSerializer(queryset, many=True)
        return Response(serializer.data)

