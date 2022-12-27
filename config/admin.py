from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Country, Language


class LanguageInline(admin.StackedInline):
    model = Language.country.through


class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'code',
        'img',
    )
    search_fields: str = ['code']
    inlines = [LanguageInline]
    fields = ['code', 'img', ]

class LanguageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'code',
        'code_name',
        'image',
        'special_font',
        'sequence'
    )
    fields = (
        'code',
        'img',
        'country',
        'special_font',
        'sequence'
    )
    readonly_fields = ('image',)

admin.site.register(Country, CountryAdmin)
admin.site.register(Language, LanguageAdmin)
