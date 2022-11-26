def render(request):
	return {
		'theme_mode': request.session.get('theme_mode', 'light')
	}
