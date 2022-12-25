from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import resolve, get_resolver
from django.utils.translation import gettext_lazy as _
from django.views import View


from itertools import chain
from operator import itemgetter

from config.models import *
from course.models import *


def index(request):
	page_title = _('Frontend')

	# course_path = get_resolver().url_patterns[4].url_patterns
	# current_url = resolve(request.path_info).url_name

	# print("current_url", current_url)

	# if current_url == '/course/':
	# 	print("current_url", current_url)

	context = {
		'title': page_title,
		# 'course_path': course_path,
	}

	return render(request,'frontend.html', context)

