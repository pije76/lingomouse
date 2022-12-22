from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View

from itertools import chain
from operator import itemgetter

from config.models import *
from course.models import *

@login_required()
def index(request):
	page_title = _('Frontend')

	course_name = 'Course'
	level_name = 'Level'
	word_name = 'Word'

	# course_titles = []
	# course_titles = course_title | level_title | word_title
	# name = course_name, level_name, word_name
	# # name = list(name)
	# name = dict({"name": name})

	# name = {{"name": course_name}}

	course_titles = {}
	# course_titles = course_titles.extend(course_name, level_name, word_name)
	course_titles.update({'name': course_name, 'name': level_name})

	# print("course_titles", course_titles)

	# path_name = request.resolver_match.view_name
	# course_path = "course:course_list"
	course_path = "/course/course/"
	# level_path = "course:level_list"
	level_path = "/course/level/"
	# word_path = "course:level_list"
	word_path = "/course/word/"

	path_url = course_path, level_path, word_path
	# path_url = list(path_url)
	path_url = dict({"path_url": path_url})

	# print("path_url", path_url)

	# course_list = course_course | course_level | course_word
	# course_list = chain(course_course, course_level, course_word)

	# for item in course_titles:
	# 	print("title", item)

	# app_list = {}
	# app_list = dict({"name": name})
	# app_list = list(name, path_url)

	# app_list = []

	app_list = [
    {
        'model': 'Course',
        'name': 'Courses',
        'object_name': 'Course',
        'admin_url': '/admin/course/course/',
        'app_url': '/admin/course/course/add/',
        'view_only': False
    },
    {
        'model': 'Level',
        'name': 'Levels',
        'object_name': 'Level',
        'admin_url': '/admin/course/level/',
        'app_url': '/admin/course/level/add/',
        'view_only': False
    },
    {
        'model': 'Word',
        'name': 'Words',
        'object_name': 'Word',
        'admin_url': '/admin/course/level/',
        'app_url': '/admin/course/level/add/',
        'view_only': False,
    }]

	# app_list.append(name)
	# app_list.append(path_url)
	# keys = ['name', 'path_url']
	# values = [name, path_url]
	# # app_list = {k: v for k, v in (('path_url', path_url))}
	# ap_list = dict(zip(keys, values))
	# # for key, value in app_list.items()

	# # results = [ item['name'] for item in ap_list ]
	# # results = map(itemgetter('name'), ap_list)
	# # results = ( item['name'] for item in ap_list )
	# results = [ item['name'] for item in ap_list ]

	# app_list = {
	# 	'name': course_name, 'path_url': '/course/course/',
	# 	'name': level_name, 'path_url': '/course/course/',
	# 	'name': word_name, 'path_url': '/course/course/',
	# }

	for item in app_list:
		print("item", item)
		print("app_list", type(item))

	context = {
		'title': page_title,
		# 'name': name,
		# 'path_url': path_url,
		# 'item': item,
		'app_list': app_list,
	}

	return render(request,'frontend.html', context)

