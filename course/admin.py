from django.contrib import admin
from django.utils.translation import gettext_lazy as _


from .forms import *
from .models import *


class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'native',
        'foreign',
        'description',
        'img',
        'is_active',
    ]
    # list_filter=['available','created','updated']
    list_editable = [
        'name',
        'native',
        'foreign',
        'img',
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


class WordAdmin(admin.ModelAdmin):
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

# Register model to Admin Panel
admin.site.register(Course, CourseAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Word, WordAdmin)

