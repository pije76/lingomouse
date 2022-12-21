from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View

from .models import *

from itertools import chain

class BulkLevelSet(View):
    def get(self, request):
        return JsonResponse({'message': 'Not implemented yet'})

    def post(self, request):
        words = request.POST.getlist('words[]')
        course_id = request.POST.get('course_id')
        level_id = request.POST.get('level_id')

        Word.objects.filter(id__in=words).update(level_id=level_id)

        return JsonResponse({'message': 'Success', 'data': course_id, 'words': words})

@login_required()
def course_list(request):
    page_title = _('Course')
    data_course =   Course.objects.all()

    course_course = Course.objects.all()
    course_level = Level.objects.all()
    course_word = Word.objects.all()

    # course_list = course_course | course_level | course_word
    course_list = chain(course_course, course_level, course_word)

    context = {
        'title': page_title,
        'data_course': data_course,
        'course_list': course_list,
    }

    return render(request,'course/course_list.html', context)

