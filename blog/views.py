from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . import models

article = models.Article.objects.get(pk=1)

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
def index(request):
    return render(request, './blog/index.html', {'test': 'hello blog', 'article': article})