from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import transaction
from django.forms.models import model_to_dict
from django.http import Http404, HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.encoding import smart_str
from django.utils.translation import gettext_lazy as _
from django.views import View

from rest_framework import generics, permissions, renderers, viewsets, status, mixins, pagination, permissions, renderers, viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from course.models import *
from course.serializers import *
from .paginations import *


class RootAPIView(APIView):
	permission_classes = (AllowAny,)
	throttle_classes = (AnonRateThrottle, UserRateThrottle,)

	def get(self, request, format=None):
		snippets = Course.objects.all()
		serializer = CourseSerializer(snippets, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = CourseSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @action(methods=['get'], detail=True)
class CourseViewSet(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer
	pagination_class = CustomPagination
	# permission_classes = [permissions.IsAuthenticated]
	# lookup_field = 'id'

	# def get_object(self):
	# 	return get_object_or_404(Course, id=self.request.query_params.get("id"))

	# def get_queryset(self):
	# 	queryset = Course.objects.filter(is_active=True).order_by('id')
	# 	return queryset

	# def perform_destroy(self, instance):
	# 	instance.is_active = False
		# instance.save()


@action(detail=True)
class CourseDetailViewSet(APIView):
	# authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication,)
	# permission_classes = [permissions.IsAuthenticated]
	# queryset = Course.objects.filter(id=id)
	# serializer_class = CourseSerializer

	def get(self, request, pk, format=None):
		item = get_object_or_404(Course.objects.all(), pk=pk)
		serializer = CourseSerializer(item)

		return Response(serializer.data)


# @csrf_exempt
@permission_classes([AllowAny])
@api_view(['GET', 'POST', ])
def course_list(request, format=None):
	serializer_context = {
		'request': request,
	}

	if request.method == 'GET':
		snippets = Course.objects.all()
		serializer_class = CourseSerializer(snippets, context=serializer_context, many=True)
		return Response(serializer_class.data)

	elif request.method == 'POST':
		serializer_class = CourseSerializer(data=request.data)
		if serializer_class.is_valid():
			serializer_class.save()
			return Response(serializer_class.data, status=status.HTTP_201_CREATED)
		return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

	# courses = CourseSerializer.objects.order_by('id').values()

	# content = {
	# 	'courses': courses,
	# }

	# return Response(content, status=200)


# @csrf_exempt
# @permission_classes([AllowAny])
@api_view(['GET', 'PUT', 'DELETE'])
def course_detail(request, pk, format=None):
	try:
		snippet = Course.objects.get(pk=pk)
	except Course.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer_class = CourseSerializer(snippet)
		return Response(serializer_class.data)

	elif request.method == 'PUT':
		serializer = SnippetSerializer(snippet, data=request.data)
		if serializer_class.is_valid():
			serializer_class.save()
			return Response(serializer_class.data)
		return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		snippet.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


# @csrf_exempt
# @permission_classes([AllowAny])
@api_view(['GET', 'POST', ])
def level_list(request, format=None):
	if request.method == 'GET':
		snippets = Level.objects.all()
		serializer = LevelSerializer(snippets, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = SnippetSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	level = Level.objects.order_by('id').values()

	content = {
		'level': level,
	}

	return Response(content, status=200)


# @csrf_exempt
# @permission_classes([AllowAny])
@api_view(['GET', 'PUT', 'DELETE'])
def level_detail(request, pk, format=None):
	try:
		snippet = Level.objects.get(pk=pk)
	except Level.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = LevelSerializer(snippet)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = SnippetSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		snippet.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



# @csrf_exempt
# @permission_classes([AllowAny])
@api_view(['GET', 'POST', ])
def word_list(request, format=None):
	if request.method == 'GET':
		snippets = Word.objects.all()
		serializer = WordSerializer(snippets, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = SnippetSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	word = Word.objects.order_by('id').values()

	content = {
		'word': word,
	}

	return Response(content, status=200)


# @csrf_exempt
# @permission_classes([AllowAny])
@api_view(['GET', 'PUT', 'DELETE'])
def word_detail(request, pk, format=None):
	try:
		snippet = Word.objects.get(pk=pk)
	except Word.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = WordSerializer(snippet)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = SnippetSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		snippet.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
