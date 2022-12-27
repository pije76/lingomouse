import pycountry
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

COUNTRY_CHOICES = [(country.alpha_2, country.name)
                   for country in pycountry.countries]
LANG_CHOICES = [(language.alpha_2, language.name)
                for language in pycountry.languages if hasattr(language, 'alpha_2')]


class TimestampedModel(models.Model):
    '''Timestamped abstract model'''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        '''Set as abstract class'''
        abstract = True


class Country(models.Model):
    '''Country'''
    code = models.CharField(
        max_length=2, verbose_name=_('Country code'), choices=sorted(COUNTRY_CHOICES, key=lambda e: e[1]), default='PL')
    img = models.ImageField(upload_to='static/image/flags/', blank=True)

    def __str__(self):
        '''Return string representation'''
        is_country = pycountry.countries.get(alpha_2=self.code)
        country = is_country.name if is_country else self.code
        return str(country)

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')


class Language(models.Model):
    '''Language model'''
    code = models.CharField(max_length=3, verbose_name=_('Language code'), choices=sorted(LANG_CHOICES, key=lambda e: e[1]), default='pl', unique=True)
    img = models.ImageField(upload_to='static/image/flags/', blank=True)
    country = models.ManyToManyField(Country, related_name='language', verbose_name=_('Country'), default='PL', blank=True)
    special_font = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.CharField(_("sequence"), max_length=2, default=0)

    def __str__(self):
        '''Return string representation'''
        is_language = pycountry.languages.get(alpha_2=self.code)
        lang = is_language.name if is_language else self.code
        return str(lang)


    def code_name(self):
        """
        Return languages code
        """
        return str(self.code)


    def image(self):
        from django.utils.html import escape
        image_file = self.img
        if(image_file != ""):
            image_file = '<img src="/uploads/%s" style="min-width:50px; min-height:50px; width:50px; height:50px; border-radius:50px; "/>' % escape(self.img)

        return mark_safe(image_file)

    image.allow_tags = True

    class Meta:
        verbose_name = _("language")
        verbose_name_plural = _("languages")
        ordering = ('sequence',)
