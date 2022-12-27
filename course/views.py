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
    # get_selected_course = request.GET.getlist('get_selected_course[]')
    # get_selected_course = request.POST.get('get_selected_course')
    # print("get_selected_course")

    # if (request.POST.get('field_is_active')) == "True":
    #     field_is_active =  "True"
    # else:
    #     field_is_active =  "False"

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
    get_language = Language.objects.all()
    native_id = Course.objects.filter(id=pk).values_list("native", flat=True).first()
    foreign_id = Course.objects.filter(id=pk).values_list("foreign", flat=True).first()
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
        'get_language': get_language,
        'native_id': native_id,
        'foreign_id': foreign_id,
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
    word = get_object_or_404(Word, id=pk)

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

    return render(request, 'course/word_detail.html', context)


def course_add(request):
    page_title = _('Add Course')
    # course = get_object_or_404(Course, id=pk)
    word = Word.objects.all()
    native_id = request.GET.get('get_selected_native', None)
    native_id = request.POST.get('get_selected_native', None)
    # print("native_id0", native_id)
    # print("native_id1", native_id)
    LANGUAGE_CHOICES = Language.objects.all().values_list("code", flat=True)
    # LANGUAGE_CHOICES = len(LANGUAGE_CHOICES)
    # LANGUAGE_CHOICES = list(LANGUAGE_CHOICES)
    # print("LANGUAGE_CHOICES", LANGUAGE_CHOICES)
    # print("LANGUAGE_CHOICES", LANGUAGE_CHOICES)

    obj = []

    for item in LANGUAGE_CHOICES:
    #     # language = pycountry.languages.lookup(item)
        language = pycountry.languages.get(alpha_2=item)
        language = language.name
        if language and language not in obj:
            obj.append(language)

    print("obj", obj)
    print("obj", type(obj))


    # for item in LANGUAGE_CHOICES:
    #     language = pycountry.languages.get(alpha_2=item).name
    #     languages.append(language)

    # for item in LANGUAGE_CHOICES:
    #     obj = pycountry.languages.get(alpha_2=item).name
    #     print("obj", obj)

    LANG_CHOICES = [(language.name)
                for language in pycountry.languages]
    # print("LANG_CHOICES", LANG_CHOICES)

    # list3 = []

    # for y in LANG_CHOICES:
    #     # print("y", y)
    #     if LANGUAGE_CHOICES == y:
    #         list3.append(y)

    list3 = set(obj) & set(LANG_CHOICES)

    # print("obj", obj)
    # print("LANG_CHOICES", LANG_CHOICES)

    tuple1 = list(list3)
    print("list3", list3)
    print("list3", type(list3))
    print("tuple1", tuple1)
    print("tuple1", type(tuple1))



    if request.method == 'POST':
        form = CourseForm(request.POST or None)
        native_id = request.GET.get('get_selected_native', None)
        native_id = request.POST.get('get_selected_native', None)
        # print("native_id2", native_id)
        # print("native_id3", native_id)

        if form.is_valid():
            course = Course()
            # course = form.save(commit=False)
            course.id = form.cleaned_data['id']
            course.name = form.cleaned_data['name']
            course.native = form.cleaned_data['native']
            # course.foreign = form.cleaned_data['foreign']
            course.description = form.cleaned_data['description']
            course.img = form.cleaned_data['img']
            course.is_active = form.cleaned_data['is_active']
            # course.save()

            return redirect('course:course_add')

    if request.method == 'GET':
        form = CourseForm()
        # form = CourseForm(prefix='course')
        native_id = request.GET.get('get_selected_native', None)
        native_id = request.POST.get('get_selected_native', None)
        # print("native_id4", native_id)
        # print("native_id5", native_id)

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
