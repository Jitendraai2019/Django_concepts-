from django.http import HttpResponse

def homepage(request):
    return HttpResponse("<h1>Hello Django, I am Jitendra</h1>")

def eggs(request):
    return HttpResponse("I love to eat eggs.")
