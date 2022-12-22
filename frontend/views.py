from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View

from itertools import chain

from config.models import *
from course.models import *

@login_required()
def index(request):
	page_title = _('Frontend')

	course_name = 'Course'
	level_name = 'Level'
	word_name = 'Word'

	course_course = Course.objects.all()
	course_level = Level.objects.all()
	course_word = Word.objects.all()

	# course_titles = []
	# course_titles = course_title | level_title | word_title
	name = course_name, level_name, word_name
	name = list(name)
	# course_titles = course_titles.extend(course_title, level_title, word_title)
	# print("name", name)

	# path_name = request.resolver_match.view_name
	# course_path = "course:course_list"
	course_path = "{% url 'course:course_list' %}"
	# level_path = "course:level_list"
	level_path = "{% url 'course:level_list' %}"
	# word_path = "course:level_list"
	word_path = "{% url 'course:level_list' %}"

	path_url = course_path, level_path, word_path
	path_url = list(path_url)

	# print("path_url", path_url)

	# course_list = course_course | course_level | course_word
	# course_list = chain(course_course, course_level, course_word)

	# for item in course_titles:
	# 	print("title", item)

	app_list = {}
	keys = ['name', 'path_url']
	values = [name, path_url]
	# app_list = {k: v for k, v in (('path_url', path_url))}
	app_list = dict(zip(keys, values))
	# for key, value in app_list.items()

	# results = [ item['name'] for item in app_list ]
	# results = ( item['name']
	# for item in app_list:
	# 	print(item['name'])

	name_list = app_list['name']
	path_url_list = app_list['path_url']

	# print("results", app_list)
	# print("app_list", type(app_list))

	context = {
		'title': page_title,
		# 'name': name,
		'path_url_list': path_url_list,
		'name_list': name_list,
	}

	return render(request,'frontend.html', context)

