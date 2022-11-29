from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views import View

from rest_framework import permissions, renderers, viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from .models import *
from .serializers import *


class BulkLevelSet(View):
	def get(self, request):
		return JsonResponse({'message': 'Not implemented yet'})

	def post(self, request):
		words = request.POST.getlist('words[]')
		course_id = request.POST.get('course_id')
		level_id = request.POST.get('level_id')

		Word.objects.filter(id__in=words).update(level_id=level_id)

		return JsonResponse({'message': 'Success', 'data': course_id, 'words': words})

# @csrf_exempt
# @permission_classes([AllowAny])
@api_view(['GET', 'POST', ])
def course_list(request, format=None):
	if request.method == 'GET':
		snippets = Course.objects.all()
		serializer = CourseSerializer(snippets, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = SnippetSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	courses = Level.objects.order_by('id').values()

	content = {
		'courses': courses,
	}

	return Response(content, status=200)


# @csrf_exempt
# @permission_classes([AllowAny])
@api_view(['GET', 'PUT', 'DELETE'])
def course_detail(request, pk, format=None):
	try:
		snippet = Course.objects.get(pk=pk)
	except Course.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = CourseSerializer(snippet)
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
