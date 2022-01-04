from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from scores.models import *


def index_view(request):
    dataset = dict()
    category = Category.objects.all()

    dataset['category'] = category
    return render(request, 'index.html', dataset)

def add_score(request):
    dataset = dict()
    category = Category.objects.all()
    return render(request, 'add_score.html', dataset)