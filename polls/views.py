from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    greetings = (
        "Hello world!, I am now coming stronger to the journey of django development."
    )
    return HttpResponse(greetings)
