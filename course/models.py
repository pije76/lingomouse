from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from config.models import TimestampedModel, Language


# Media Type
AUDIO = 'AUDIO'
VIDEO = 'VIDEO'
IMAGE = 'IMAGE'
MEDIA_TYPE = (
    (AUDIO, 'Audio'),
    (VIDEO, 'Video'),
    (IMAGE, 'Image')
)


class OnlyActiveManager(models.Manager):
    def get_queryset(self):
        return super(OnlyActiveManager, self).get_queryset().filter(is_active=True)

class Course (models.Model):
    '''
    Course models with fields {`name`, `description`, `native`, `foreign`} and a list of levels
    '''
    lookup_field = "id"
    id = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=200)
    native = models.ForeignKey(Language, related_name='native_courses', verbose_name=_("native"), on_delete=models.RESTRICT)
    foreign = models.ForeignKey(Language, related_name='foreign_courses', verbose_name=_("foreign"), on_delete=models.RESTRICT)
    description = models.TextField(max_length=1000, verbose_name=_("description"), null=True, blank=True)
    img = models.ImageField(upload_to='images/', blank=True)
    is_active = models.BooleanField(_("Is active?"), default=True)

    class Meta:
        indexes = [models.Index(fields=["name"])]
        ordering = ["name"]
        verbose_name = _("course")
        verbose_name_plural = _("courses")

    def __str__(self):
        return str(self.name)

    def word_count(self):
        if hasattr(self, 'words'):
            return self.words.count()
        return 0

    def mastered_word_count(self):
        calculate_mastered_word_count = 1
        return calculate_mastered_word_count

    def progress(self):
        calculate_progress = self.mastered_word_count()/self.words.count()
        return round(calculate_progress, 5)


    def image(self):
        from django.utils.html import escape
        image_file = self.img
        if(image_file != ""):
            image_file = '<img src="/uploads/%s" style="min-width:50px; min-height:50px; width:50px; height:50px; border-radius:50px; "/>' % escape(self.img)

        return mark_safe(image_file)

    image.allow_tags = True

    def get_absolute_url(self):
        return reverse('course:course_list', args=[self.id])


class Level (TimestampedModel):
    """
    Level models each level has a name and a list of words
    """
    sequence = models.IntegerField(default=0, verbose_name=_("sequence"))
    name = models.CharField(max_length=200, verbose_name=_("name"), default=_("Level"))
    course = models.ForeignKey(Course, related_name='levels', verbose_name=_("course"), on_delete=models.CASCADE, blank=True)

    def __str__(self):
        '''String representation'''
        return str(self.course)+' - '+str(self.name)

    class Meta:
        ordering = ["sequence"]
        verbose_name = "level"
        verbose_name_plural = "levels"

    def word_count(self):
        if hasattr(self, 'level_words'):
            return self.level_words.count()
        return 0

    def level_count(self):
        calculate_mastered_word_count = 1
        return calculate_mastered_word_count

    def level_progress(self):
        calculate_progress = self.level_count()/self.level_words.count()
        return round(calculate_progress, 5)

    def get_absolute_url(self):
        return reverse('course:course_list', args=[self.id])


class Word (TimestampedModel):
    """
    Word models inherited from timestamped model
    """
    objects = models.Manager()
    actives = OnlyActiveManager()

    word = models.CharField(max_length=200, verbose_name=_("foreign"))
    description = models.CharField(max_length=200, verbose_name=_("native"), default="")
    literal_translation = models.CharField(max_length=200, verbose_name=_("literal translation"), default="", blank=True)
    course = models.ForeignKey('Course', related_name='words', on_delete=models.CASCADE)
    level = models.ForeignKey("Level", related_name="level_words", on_delete=models.SET_NULL, blank=True, null=True)
    is_active = models.BooleanField(_("Is active"), default=True)

    def __str__(self):
        return str(self.word + ' - ' + self.description)

    class Meta:
        verbose_name = _("word")
        verbose_name_plural = _("words")
        ordering = ["level__sequence", "created_at"]


    def get_absolute_url(self):
        return reverse('course:course_list', args=[self.id])


class WordMedia(TimestampedModel):
    """
    Word media models
    """
    media_type = models.CharField(choices=MEDIA_TYPE, default=IMAGE, max_length=200)
    word = models.ForeignKey(
        Word, related_name="medias", on_delete=models.CASCADE)
    path_to_file = models.FileField(upload_to='word/', blank=True)

    def __str__(self):
        return str(self.media_type)

    class Meta:
        verbose_name = _("word media")
        verbose_name_plural = _("word medias")

    def get_path(self):
        '''Get path to file'''
        return format_html(
            '<a href="{}">{}</a>',
            self.path_to_file,
            self.media_type
        )
