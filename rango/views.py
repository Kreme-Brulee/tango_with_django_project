from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner!\nHere is a link to the about page: (<a href='/rango/about/'>About</a>)")
    
def about(request):
    return HttpResponse("Rango says here is the about page.\nHere is a link to the index page: (<a href='/rango/'>Index</a>)")
