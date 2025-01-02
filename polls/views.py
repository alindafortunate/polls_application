from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    greetings = "Hello world!, Working on the polls app."
    return HttpResponse(greetings)


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    response = "You're looking at the results of question"
    return HttpResponse(f"{response} {question_id}.")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
