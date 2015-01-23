from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there world!<br/> <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("This tutorial has been put together by Anton Todorov, 2085359T<br/>Rango says here is the about page.<br/><a href='/rango/'>Index</a>")

def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    context_dict = {}
    return render(request, 'rango/about.html', context_dict)
