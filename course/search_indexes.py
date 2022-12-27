from django.utils import timezone

from haystack import indexes
from haystack.fields import CharField

from .models import *

import datetime

class CourseIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True, template_name='/var/www/html/lingomouse/theme/templates/course/indexes/course/course_text.txt')
    # text = indexes.CharField(document=True, use_template=True)
    # name = indexes.CharField(model_attr='name', faceted=True)
    name = indexes.EdgeNgramField(model_attr='name')
    native = indexes.EdgeNgramField(model_attr='native')
    foreign = indexes.EdgeNgramField(model_attr='foreign')
    description = indexes.EdgeNgramField(model_attr="description", null=True)
    # native = indexes.CharField(model_attr='native', faceted=True)

    # We add this for autocomplete.
    # name_auto = indexes.EdgeNgramField(model_attr='name')

    # suggestions = indexes.FacetCharField()

    def get_model(self):
        return Course

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        # return self.get_model().objects.filter(is_active="True")
        return Course.objects.filter(is_active="True")
