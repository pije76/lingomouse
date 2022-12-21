from django import template

from config.models import *
from course.models import *

register = template.Library()

@register.simple_tag
def app_list():

	course_course = Course.objects.all()
	course_level = Level.objects.all()
	course_word = Word.objects.all()

	course_list = config_country | config_language

	config_country = Country.objects.all()
	config_language = Language.objects.all()

	config_list = config_country | config_language

	app_list = course_list | config_list

	return app_list
