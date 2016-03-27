from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    mydict = {'varA':1000, 'varB':'hello itcast', 'varC':3.14}
    return render(request, 'rango/index.html', mydict)

def teacher(request):
    return HttpResponse('hello everyone')
