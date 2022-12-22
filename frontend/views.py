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

	course_title = 'Course'
	level_title = 'Level'
	word_title = 'Word'

	course_course = Course.objects.all()
	course_level = Level.objects.all()
	course_word = Word.objects.all()

	# course_titles = []
	# course_titles = course_title | level_title | word_title
	course_titles = course_title, level_title, word_title
	course_titles = list(course_titles)
	# course_titles = course_titles.extend(course_title, level_title, word_title)

	# course_list = course_course | course_level | course_word
	course_list = chain(course_course, course_level, course_word)

	for item in course_titles:
		print("title", item)

	context = {
		'title': page_title,
		'course_titles': course_titles,
		'course_list': course_list,
	}

	return render(request,'frontend.html', context)

