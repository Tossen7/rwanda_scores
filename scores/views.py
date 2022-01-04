from django.shortcuts import render
from .forms import *

# Create your views here.
def score_create(erquest):
    if request.method == 'POST'
    form = AddingScoreForm(request.POST, request.FILES)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.author = request.POST.get('author')
        instance.file = request.FILES.get('files')
        instance.category = request.POST.get('category')
        instance.comments = request.POST.get('comments')

        instance.save()

        return redirect('')
    else:
        messages.error(request, 'Error adding a score')
        return redirect('')

    dataset = dict()
    form = AddingScoreForm()
    dataset['form'] = form
    return render(request, 'add_score.html', dataset)
    
    
