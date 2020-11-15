from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def question(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    context = {
        'question' : question,
    }
    return render(request,'questions/question.html',context)
    