from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View

from .models import *
from .forms import *

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


def course_index(request):
    page_title = _('Select course to change')

    context = {
        'title': page_title,
    }

    return render(request,'course/course_index.html', context)


def course_list(request):
    page_title = _('Select course to change')
    data_course =   Course.objects.all()

    print("data_course", data_course)

    context = {
        'title': page_title,
        'data_course': data_course,
    }

    return render(request,'course/course_list.html', context)


def level_list(request):
    page_title = _('Select level to change')
    data_level =   Level.objects.all()


    context = {
        'title': page_title,
        'data_level': data_level,
    }

    return render(request,'course/level_list.html', context)



def word_list(request):
    page_title = _('Select word to change')
    data_word =   Word.objects.all()


    context = {
        'title': page_title,
        'data_word': data_word,
    }

    return render(request,'course/word_list.html', context)


def change_course(request, pk):
    page_title = _('Change Course')
    form = CourseForm(prefix='course')

    if request.method == 'POST':
        form = CourseForm(request.POST or None, instance=request.user)

        if form.is_valid():
            course = form.save(commit=False)
            course.full_name = form.cleaned_data['full_name']
            course.email = form.cleaned_data['email']
            course.ic_number = form.cleaned_data['ic_number']
            course.save()

            messages.success(request, _('Your course has been change successfully.'))
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)

    else:
        form = CourseForm(instance=request.user)

    context = {
        'title': page_title,
        'form': form,
    }

    return render(request, 'course/course_change.html', context)



def change_level(request, pk):
    page_title = _('Change Level')
    form = CourseForm(prefix='course')

    if request.method == 'POST':
        form = CourseForm(request.POST or None, instance=request.user)

        if form.is_valid():
            course = form.save(commit=False)
            course.full_name = form.cleaned_data['full_name']
            course.email = form.cleaned_data['email']
            course.ic_number = form.cleaned_data['ic_number']
            course.save()

            messages.success(request, _('Your course has been change successfully.'))
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)

    else:
        form = CourseForm(instance=request.user)

    context = {
        'title': page_title,
        'form': form,
    }

    return render(request, 'course/level_change.html', context)

