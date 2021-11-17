from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.files import ImageField
from django.utils import timezone
from django.utils.translation import ugettext as _

# Create your models here.

class Category(models.Model):
    name = models.CharField(_('Category'), max_length=250, blank=False, null=False)
    created_at = models.DateTimeField(_('Date'), auto_now_add=True)