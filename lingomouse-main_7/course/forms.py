from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms.models import BaseInlineFormSet

from .models import MEDIA_TYPE, Level
from theme.widgets.widgets import MediaFileInput


class CourseForm(forms.ModelForm):
    '''Account form'''
    id = forms.CharField(max_length=200)
    name = forms.CharField(max_length=200)
    description = forms.CharField(max_length=1000, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control text-area'})



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
