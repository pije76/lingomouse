from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import *

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


@login_required()
def country_list(request):
    page_title = _('Country')
    data_country =   Country.objects.all()

    context = {
        'title': page_title,
        'data_country': data_country,
    }

    return render(request,'config/config_set.html', context)


def language_list(request):
    page_title = _('Languages')
    data_language =   Languages.objects.all()

    context = {
        'title': page_title,
        'data_language': data_language,
    }

    return render(request,'config/config_set.html', context)

