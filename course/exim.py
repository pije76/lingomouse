from import_export import resources

from .models import *


class WordResource(resources.ModelResource):
    class Meta:
        model = Word
