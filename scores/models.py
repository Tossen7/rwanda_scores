from datetime import datetime
from django.db.models.deletion import CASCADE
from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields.files import ImageField
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
# Create your models here.
#model for category

class Category(models.Model):
    name = models.CharField(_('Category'),max_length=250,blank=False, null=False)
    created = models.DateTimeField(_('Date'), auto_now_add = True)


    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['created']


    def __str__(self):
        return self.name
#model for score
class Score(models.Model):

    author = models.CharField(_('Author'), max_length = 250, blank = True, null = True)
    file = models.FileField(_('Music Sheet'), upload_to='', blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name = _('Category'),default=1, max_length=200, on_delete=CASCADE, blank=False, null=False)
    comments = models.TextField(_('Comment'),blank= False, null=False, default='Helping people to pray')
    publication_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=datetime.now())


    class Meta:
        verbose_name = _('Score')
        verbose_name_plural = _('Scores')
        ordering = ['created']


    def __str__(self):
        return self.file

class Status(models.Model):
    name = models.CharField(_('Status'), max_length=250, default='PENDING')
    created = models.DateTimeField(_('Created'), auto_now_add=datetime.now())

class Advert(models.Model):
    
    image = models.ImageField(_('Image'))
    title = models.CharField(_('Title'), max_length=250, blank=True, null=True)
    short_description = models.TextField(_('Short Description'), blank=True, null=True)
    link = models.CharField(_('Link'), blank=True, null=True, max_length=250)
    status = models.ForeignKey(_('Status'), blank=False, null=False, on_delete=CASCADE)
    created = models.DateTimeField(_('Create'), auto_now_add=datetime.now())

    class Meta:
        verbose_name = _('Advert')
        verbose_name_plural = _('Adverts')
        ordering = ['created']

    def __str__(self):
        return self.link