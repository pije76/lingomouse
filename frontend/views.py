from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View

@login_required()
def index(request):
    page_title = _('Frontend')

    context = {
        'title': page_title,
    }

    return render(request,'frontend.html', context)

