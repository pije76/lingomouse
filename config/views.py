from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


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
