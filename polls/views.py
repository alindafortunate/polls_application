from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    result = []
    for q in latest_question_list:
        result.append(q.question_text)
    output = ", ".join(result)
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    response = "You're looking at the results of question"
    return HttpResponse(f"{response} {question_id}.")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
