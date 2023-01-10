from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from import_export.admin import ImportExportModelAdmin

from .forms import *
from .models import *


class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'native',
        'foreign',
        'description',
        'image',
        'is_active',
    ]
    # list_filter=['available','created','updated']
    list_editable = [
        'name',
        'native',
        'foreign',
        # 'img',
        'is_active',
    ]


class LevelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'sequence',
        'name',
        'course',
    ]
    # list_filter=['available','created','updated']
    list_editable = [
        'sequence',
        'name',
        'course',
    ]

    ordering = ('sequence', 'id',)


class WordAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'word',
        'description',
        'literal_translation',
        'course',
        'level',
        'is_active',
    ]
    # list_filter=['available','created','updated']
    list_editable = [
        'word',
        'description',
        'literal_translation',
        'course',
        'level',
        'is_active',
    ]

    ordering = ('course', 'id',)


# Register model to Admin Panel
admin.site.register(Course, CourseAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Word, WordAdmin)

