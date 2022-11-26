from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .forms import WordMediaForm, WordChangeListForm, WordForm, WordInlineForm
from .models import Course, Level, Word, WordMedia


class WordMediaAcquaintanceInline(admin.TabularInline):
    '''show word models as inline in Level'''
    model = WordMedia
    extra = 0
    form = WordMediaForm
    template = "course/edit_inline/word_inline.html"


class WordAcquaintanceInline(admin.TabularInline):
    '''show word models as inline in Level'''
    model = Word
    fields = ['id', 'word', 'description', 'level']
    extra = 1
    readonly_fields = ['id']
    max_num: int = 20
    show_full_result_count: bool = True
    show_change_link: bool = True


class WordWithFKAdminInline(admin.TabularInline):
    per_page = 20
    model = Word
    fields = ('pk', 'word', 'description',
              'level', 'is_active')
    readonly_fields = ['pk']
    show_change_link: bool = True
    sortable_by = ('pk', 'is_active')
    form = WordForm
    formset = WordInlineForm
    template = "admin/edit_inline/tabular_word.html"

    def get_formset(self, request, obj, **kwargs):
        return super().get_formset(request, obj, **kwargs)
    

class LevelAcquaintanceInline(admin.TabularInline):
    '''show level models as inline in Level'''
    model = Level
    fields = ['pk', 'sequence', 'name']
    extra = 0
    readonly_fields = ['pk']
    show_change_link = True


class CourseAdmin(admin.ModelAdmin):
    """Course admin"""
    list_filter = ['is_active']
    readonly_fields = ['image', ]
    list_display = ('pk', 'name', 'description', 'native',
                    'foreign', 'image', 'is_active')
    search_fields = ['id', 'name', 'description']
    fieldsets = (
        (None, {'classes': ('shadow-lg rounded',),
         'fields': ('id', 'name', 'native', 'foreign', 'description', 'image', 'img', 'is_active')}),
    )
    inlines = [LevelAcquaintanceInline, WordWithFKAdminInline]
    save_on_top = True
    change_form_template = "course/change_course.html"
    template_name = "course/course_view.html"
    dashboard_template = "admin/dashboard.html"
    actions = ['set_active', 'set_inactive']

    def render_change_form(self, request, context, *args, **kwargs):
        obj = kwargs.get('obj', None)
        if obj:
            context.update(levels=obj.levels.all())
        context.update(obj=obj)

        return super(CourseAdmin, self).render_change_form(request, context, *args, **kwargs)


class LevelAdmin(admin.ModelAdmin):
    '''Level admin'''
    list_display = ['id', 'name', 'course', 'word_count']
    search_fields = ['id', 'name', 'course']
    ordering = ['sequence']
    inlines = [WordAcquaintanceInline]
    fields = ['sequence', 'name', 'course']

    class Meta:
        '''Meta class'''
        model = Level


class WordAdmin(admin.ModelAdmin):
    """Word model admin"""
    list_display = ['id', 'word', 'description', 'course', 'level', 'is_active']
    search_fields = ['id', 'word', 'description', 'is_active']
    list_filter = ('is_active',)
    ordering = ['-is_active', 'id']
    list_display_links = ('id',)
    list_per_page: int = 40
    list_editable = ('word', 'description', 'level')
    inlines = [WordMediaAcquaintanceInline]
    actions = ['set_archived', 'set_active']
    change_form_template = "course/change_word.html"

    class Meta:
        """Set model"""
        model = Word

    def get_changelist_form(self, request, *args, **kwargs):
        return WordChangeListForm

    def formfield_for_foreignkey(self, db_field, request, *args, **kwargs):
        if db_field.name == 'level':
            kwargs['queryset'] = Level.objects \
                .prefetch_related('course') \
                .select_related('course')

        return super().formfield_for_foreignkey(db_field, request, *args, **kwargs)


# Register model to Admin Panel
admin.site.register(Course, CourseAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Word, WordAdmin)