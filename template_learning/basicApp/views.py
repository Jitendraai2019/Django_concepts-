from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'text':'Hello World','number':100}
    return render(request,'basicApp/index.html',context_dict)

def other(request):
    return render(request,'basicApp/other.html')

def relative(request):
    return render(request,'basicApp/relative_url_templates.html')
