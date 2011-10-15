from django.http import HttpResponse
from django.template import Context, loader
from entries.models import Recipe, Ingredient
from django.shortcuts import render_to_response

def index(request):
    alpha = Recipe.objects.all().order_by('title')
    return render_to_response('index.html', {'alpha': alpha})