from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html',{'hi_there': 'This is me form view.py file!'})

def eggs(request):
    return HttpResponse("<h1>I love to eat eggs.</h1>")
