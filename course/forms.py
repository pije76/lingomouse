from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms.models import BaseInlineFormSet

from config.models import *

from .models import *
from .widgets import *


class CourseForm(forms.Form):
	LANGUAGE_CHOICES = Language.objects.all().values_list("code", flat=True)

	id = forms.CharField(label=_(u''), required=True, max_length=200, widget=forms.TextInput(attrs={'class': "vTextField"}))
	name = forms.CharField(label=_(u''), required=True, max_length=200, widget=forms.TextInput(attrs={'class': "vTextField"}))
	description = forms.CharField(label=_(u''), required=False, max_length=1000, widget=forms.Textarea(attrs={'class': "vLargeTextField", 'cols': 40, 'rows': 10}))
	# native = forms.ChoiceField(label=_(u''), required=False, widget=forms.Select, choices=((x.id, x.name) for x in LANGUAGE_CHOICES))
	native = forms.ChoiceField(label=_(u''), required=False, choices=(LANGUAGE_CHOICES), widget=forms.Select)
	foreign = forms.ChoiceField(label=_(u''), required=False, choices=(LANGUAGE_CHOICES), widget=forms.Select)
	img = forms.ImageField(label=_(u''), required=False)


class CourseModelForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = '__all__'
		widgets = {
			# 'patient': forms.HiddenInput(),
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['id'].widget.attrs.update({'class': 'form-control'})
		self.fields['name'].widget.attrs.update({'class': 'form-control'})
		self.fields['description'].widget.attrs.update({'class': 'form-control text-area'})

	'''Account form'''
	id = forms.CharField(max_length=200)
	name = forms.CharField(max_length=200)
	description = forms.CharField(max_length=1000, required=False)


# Word Media Form
class WordMediaForm(forms.ModelForm):
	""" If field type is field then add recorder to """
	media_type = forms.ChoiceField(choices=MEDIA_TYPE)
	path_to_file = forms.FileField(
		widget=MediaFileInput)


class WordChangeListForm(forms.ModelForm):
	""" Filter level by own course """
	def __init__(self, *args, **kwargs):
		super(WordChangeListForm, self).__init__(*args, **kwargs)

		if self.instance:
			_level_queryset = Level.objects.filter(course_id=self.instance.course.id)

			self.fields['level'].queryset = _level_queryset
			self.fields['level'].choices = [(level.id, level.name) for level in _level_queryset]


class WordForm(forms.ModelForm):
	def __init__(self, *args, parent_object, **kwargs):
		self.parent_object = parent_object
		super(WordForm, self).__init__(*args, **kwargs)


class WordInlineForm(BaseInlineFormSet):
	""" Filter level by own course """
	def __init__(self, *args, **kwargs) -> None:
		super(WordInlineForm, self).__init__(*args, **kwargs)

		if self.instance:
			_level_queryset = Level.objects.filter(course_id=self.instance.id)

			for form in self.forms:
				form.fields['level'].queryset = _level_queryset
				form.fields['level'].choices = [(level.id, level.name) for level in _level_queryset]

	def get_form_kwargs(self, index):
		kwargs = super().get_form_kwargs(index)
		kwargs['parent_object'] = self.instance
		return kwargs
