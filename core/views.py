from django.shortcuts import HttpResponse, render


# Create your views here.
def index(request):
    return HttpResponse("Hello World. You are in the page index")
