from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
def index(request):
    return render(request, './blog/index.html', {'test': 'hello blog2'})