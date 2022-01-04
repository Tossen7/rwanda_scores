from django import forms
from django.contrib.auth import models
from django.db.models.base import Model
from .models import *


#Adding score

class AddingScoreForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['created', 'publication_date']