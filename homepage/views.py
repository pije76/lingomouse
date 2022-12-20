from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View

@login_required()
def homepage(request):
    page_title = _('homepage')

    context = {
        'page_title': page_title,
    }

    return render(request,'homepage.html', context)

