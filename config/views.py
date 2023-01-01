from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .forms import *

@method_decorator(csrf_exempt, name='dispatch')
class SetupThemeMode(View):
    def post(self, request, *args, **kwargs):
        theme_mode = 'dark'
        if request.session.get('theme_mode', 'dark') == 'dark':
            theme_mode = 'light'
        else:
            theme_mode = 'dark'
        request.session['theme_mode'] = theme_mode

        return JsonResponse({**request.session})


setup_theme_mode = SetupThemeMode.as_view()

def config_index(request):
    page_title = _('Select config to change')

    context = {
        'title': page_title,
    }

    return render(request,'config/config_index.html', context)


################# COUNTRY VIEW #############
def country_list(request):
    page_title = _('Select country to change')
    country_list =   Country.objects.all()

    context = {
        'title': page_title,
        'country_list': country_list,
    }

    return render(request,'config/country_list.html', context)



def country_detail(request, pk):
    page_title = _('Change Country')
    country = get_object_or_404(Country, id=pk)

    form = CountryForm(prefix='country')

    if request.method == 'POST':
        form = CountryForm(request.POST or None, instance=request.user)

        if form.is_valid():
            country = form.save(commit=False)
            country.full_name = form.cleaned_data['full_name']
            country.email = form.cleaned_data['email']
            country.ic_number = form.cleaned_data['ic_number']
            country.save()

            messages.success(request, _('Your country has been change successfully.'))
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)

    else:
        form = CountryForm()

    context = {
        'title': page_title,
        'form': form,
        'country': country,
    }

    return render(request, 'config/country_detail.html', context)


def country_add(request):
    page_title = _('Change Country')
    # country = get_object_or_404(Country, id=pk)
    word = Word.objects.all()

    form = CountryForm(prefix='country')

    if request.method == 'POST':
        form = CountryForm(request.POST or None, instance=request.user)

        if form.is_valid():
            country = form.save(commit=False)
            country.full_name = form.cleaned_data['full_name']
            country.email = form.cleaned_data['email']
            country.ic_number = form.cleaned_data['ic_number']
            country.save()

            messages.success(request, _('Your country has been change successfully.'))
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)

    else:
        form = CountryForm()

    context = {
        'title': page_title,
        'form': form,
        'word': word,
    }

    return render(request, 'config/country_add.html', context)


def country_delete(request, pk):
    country_data = get_object_or_404(Country, id=pk)
    country_data.delete()

    return redirect('country:country_list')

################# COUNTRY VIEW #############
def language_list(request):
    page_title = _('Languages')
    language_list =   Language.objects.all()

    context = {
        'title': page_title,
        'language_list': language_list,
    }

    return render(request,'config/language_list.html', context)


def language_detail(request, pk):
    page_title = _('Change Country')
    language = get_object_or_404(Language, id=pk)

    # form = LanguageForm(prefix='language')

    if request.method == 'POST':
        form = LanguageForm(request.POST or None, instance=request.user)

        if form.is_valid():
            language = form.save(commit=False)
            language.full_name = form.cleaned_data['full_name']
            language.email = form.cleaned_data['email']
            language.ic_number = form.cleaned_data['ic_number']
            language.save()

            messages.success(request, _('Your language has been change successfully.'))
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)

    else:
        form = LanguageForm()

    context = {
        'title': page_title,
        'form': form,
        'language': language,
    }

    return render(request, 'config/language_detail.html', context)


def language_add(request):
    page_title = _('Change Language')
    # language = get_object_or_404(Language, id=pk)
    word = Word.objects.all()

    form = LanguageForm(prefix='language')

    if request.method == 'POST':
        form = LanguageForm(request.POST or None, instance=request.user)

        if form.is_valid():
            language = form.save(commit=False)
            language.full_name = form.cleaned_data['full_name']
            language.email = form.cleaned_data['email']
            language.ic_number = form.cleaned_data['ic_number']
            language.save()

            messages.success(request, _('Your language has been change successfully.'))
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)

    else:
        form = LanguageForm()

    context = {
        'title': page_title,
        'form': form,
        'word': word,
    }

    return render(request, 'config/language_add.html', context)
