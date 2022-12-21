from config.models import *
from course.models import *

from itertools import chain


# def app_list(context):
def app_list(request):

	course_course = Course.objects.all()
	course_level = Level.objects.all()
	course_word = Word.objects.all()

	# course_list = course_course | course_level | course_word
	# course_list = chain(course_course, course_level, course_word)


	config_country = Country.objects.all()
	config_language = Language.objects.all()

	# config_list = config_country | config_language
	# config_list = chain(config_country, config_language)

	# app_list = course_list | config_list

	app_list = chain(course_course, course_level, course_word, config_country, config_language)

	context = {
		# 'produits':produits,
		# 'categories':categories,
		'app_list': app_list,
	}

	for item in app_list:
	    print("app_list", item)

	return context

	# return {
	#     'app_list' : app_list,
	# }
