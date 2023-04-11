from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import transaction
from django.forms.models import model_to_dict
from django.http import Http404, HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.encoding import smart_str
from django.utils.translation import gettext_lazy as _
from django.views import View

# from rest_framework import generics, permissions, renderers, viewsets, status, mixins, pagination
from rest_framework import status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse, reverse_lazy
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import TemplateHTMLRenderer

from allauth.socialaccount.providers.apple.client import AppleOAuth2Client
from allauth.socialaccount.providers.apple.views import AppleOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

# from dj_rest_auth.registration.views import SocialConnectView
from dj_rest_auth.registration.views import SocialLoginView

# from .googleviews import GoogleOAuth2AdapterIdToken

# from oauth2_provider.views.generic import ProtectedResourceView
# from oauth2_provider.decorators import protected_resource


from course.models import *
from course.serializers import *

from .paginations import *


@api_view(['GET'])
@permission_classes([AllowAny,])
def api_root(request, format=None):
    return Response({
        'courses': reverse_lazy('course_list', request=request, format=format),
        'levels': reverse_lazy('level_list', request=request, format=format)
    })


@api_view(['GET', 'POST'])
@permission_classes([AllowAny,])
def course_list(request):
    list_course = Course.objects.all().order_by('id')
    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(list_course, request)
    renderer_classes = [TemplateHTMLRenderer]
    
    # progress = serializers.SerializerMethodField(read_only=True)
    # progress = ProgressField()
    # get_course = Course.objects.all()
    # total_progress = serializers.SerializerMethodField()
    # # get_course = Course.objects.filter(course=obj).count()
    # # get_progress = get_course.progress()
    # xxx = [x for x in get_course if x.progress()]

    if request.method == 'GET':
    # if request.method == 'GET' and request.accepted_renderer.format == 'html':
        serializer = CourseSerializer(list_course, many=True, context={'request': request})
        response = paginator.get_paginated_response(serializer.data)

        # response.data['Course Progress'] = get_progress
        response.data['Level List'] = reverse_lazy('level_list', request=request)
        response.data['Word List'] = reverse_lazy('word_list', request=request)
        
        # return Response(serializers.data)
        return Response(response.data, status=200)

    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
    #     serializer = CourseSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
        # return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return paginator.get_paginated_response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny,])
def level_list(request):
    list_level = Level.objects.all().order_by('id')
    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(list_level, request)
    serializer = LevelSerializer(list_level, many=True)

    if request.method == 'GET':
        return paginator.get_paginated_response(serializer.data)    
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny,])
def word_list(request):
    list_word = Word.objects.all().order_by('id')
    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(list_word, request)
    serializer = WordSerializer(list_word, many=True)

    if request.method == 'GET':
        return paginator.get_paginated_response(serializer.data)    
    return paginator.get_paginated_response(serializer.data)


class Api_RootView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]    

    def get(self, request, format=None):
        list_course = Course.objects.all().order_by('id')
        list_level = Level.objects.all().order_by('id')

        list_course = reverse_lazy('course_list', request=request)
        list_level = reverse_lazy('level_list', request=request)
        serializer = CourseSerializer(list_course, many=True)

        return Response({
            "courses": list_course,
            "levels": list_level,
        })


# class CourseViewSet(ModelViewSet, ProtectedResourceView):
class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all().order_by('id')
    serializer_class = CourseSerializer
    pagination_class = CustomPagination
    # permission_classes = (IsAuthenticated,)
    authentication_classes=[TokenAuthentication]


class LevelViewSet(ModelViewSet):
    queryset = Level.objects.all().order_by('id')
    serializer_class = LevelSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)
    authentication_classes=[TokenAuthentication]

    def get(self, request, format=None):
        queryset = Level.objects.all()
        serializer = LevelSerializer(queryset, many=True)
        return Response(serializer.data)


@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    # adapter_class = GoogleOAuth2AdapterIdToken
    client_class = OAuth2Client
    # callback_url = "http://127.0.0.1:8000/auth/google/callback/"
    # callback_url = "http://127.0.0.1:8000/accounts/google/login/callback/"
    callback_url = "http://127.0.0.1:8000/api/"
    # callback_url = getattr(settings, 'SOCIAL_LOGIN_GOOGLE_CALLBACK_URL', '127.0.0.1:8000')
    # authentication_classes = ([])


class AppleLogin(SocialLoginView):
    adapter_class = AppleOAuth2Adapter
    client_class = AppleOAuth2Client
    # callback_url = "http://127.0.0.1:8000/auth/apple/callback/"
#     callback_url = 'http://127.0.0.1:8000/accounts/apple/login/callback/'
    # callback_url = f"{settings.BACKEND_URL}api/v1/user/auth/apple/callback/"
    callback_url = "http://127.0.0.1:8000/api/"
