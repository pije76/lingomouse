from django import template

from itertools import chain

from config.models import *
from course.models import *

register = template.Library()

@register.simple_tag(takes_context=True)
def url_active(context, *args, **kwargs):
	if 'request' not in context:
		return ''

	request = context['request']
	if request.resolver_match.url_name in args:
		return kwargs['active'] if 'active' in kwargs else 'inactive'
	else:
		return 'border-white text-gray-500'

@register.simple_tag(takes_context=True)
def suburl_active(context, *args, **kwargs):
	if 'request' not in context:
		return ''

	request = context['request']
	if request.resolver_match.url_name in args:
		return kwargs['active'] if 'active' in kwargs else 'inactive'
	else:
		return ''
