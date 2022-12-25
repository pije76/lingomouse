from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
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
    page_title = _('Course')

    context = {
        'title': page_title,
    }

    return render(request,'course/course_index.html', context)


def course_list(request):
    page_title = _('Select course to change')
    data_course =   Course.objects.all()

    if (request.POST.get('field_is_active')) == "True":
        field_is_active =  "True"
    else:
        field_is_active =  "False"

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
    course_id = request.POST.get('course')
    data_word =   Word.objects.all()
    level_items = Level.objects.filter(course=course_id)

    context = {
        'title': page_title,
        'data_word': data_word,
        'level_items': level_items,
    }

    return render(request,'course/word_list.html', context)


def course_detail(request, pk):
    page_title = _('Change Course')
    course = get_object_or_404(Course, id=pk)
    word = Word.objects.all()

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
        form = CourseForm()

    context = {
        'title': page_title,
        'form': form,
        'course': course,
        'word': word,
    }

    return render(request, 'course/course_detail.html', context)


def level_detail(request, pk):
    page_title = _('Change Level')
    form = CourseForm(prefix='level')
    level = get_object_or_404(Level, id=pk)

    if request.method == 'POST':
        form = CourseForm(request.POST or None, instance=request.user)

        if form.is_valid():
            level = form.save(commit=False)
            level.full_name = form.cleaned_data['full_name']
            level.email = form.cleaned_data['email']
            level.ic_number = form.cleaned_data['ic_number']
            level.save()

            messages.success(request, _('Your level has been change successfully.'))
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)

    else:
        form = CourseForm()

    context = {
        'title': page_title,
        'form': form,
        'level': level,
    }

    return render(request, 'course/level_detail.html', context)


def word_detail(request, pk):
    page_title = _('Change Word')
    form = CourseForm(prefix='word')

    if request.method == 'POST':
        form = CourseForm(request.POST or None, instance=request.user)

        if form.is_valid():
            word = form.save(commit=False)
            word.full_name = form.cleaned_data['full_name']
            word.email = form.cleaned_data['email']
            word.ic_number = form.cleaned_data['ic_number']
            word.save()

            messages.success(request, _('Your word has been change successfully.'))
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)

    else:
        form = CourseForm()

    context = {
        'title': page_title,
        'form': form,
    }

    return render(request, 'course/word_detail.html', context)


def course_add(request):
    page_title = _('Change Course')
    # course = get_object_or_404(Course, id=pk)
    word = Word.objects.all()

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
        form = CourseForm()

    context = {
        'title': page_title,
        'form': form,
        'word': word,
    }

    return render(request, 'course/course_add.html', context)


def level_add(request):
    page_title = _('Change Course')
    # course = get_object_or_404(Course, id=pk)
    word = Word.objects.all()

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
        form = CourseForm()

    context = {
        'title': page_title,
        'form': form,
        'word': word,
    }

    return render(request, 'course/level_add.html', context)


def word_add(request):
    page_title = _('Change Course')
    # word = get_object_or_404(Course, id=pk)
    word = Word.objects.all()

    form = CourseForm(prefix='word')

    if request.method == 'POST':
        form = CourseForm(request.POST or None, instance=request.user)

        if form.is_valid():
            word = form.save(commit=False)
            word.full_name = form.cleaned_data['full_name']
            word.email = form.cleaned_data['email']
            word.ic_number = form.cleaned_data['ic_number']
            word.save()

            messages.success(request, _('Your word has been change successfully.'))
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)

    else:
        form = CourseForm()

    context = {
        'title': page_title,
        'form': form,
        'word': word,
    }

    return render(request, 'course/word_add.html', context)
