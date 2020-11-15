from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Module
from questions.models import Question
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def home(request):
    modules = Module.objects.order_by('-mod_date').filter(is_Published=True)
    paginator = Paginator(modules, 6)
    page = request.GET.get('page')
    paged_modules = paginator.get_page(page)
    context = {
        'modules' : paged_modules
    }
    return render(request,'modules/home.html',context)   

def module(request, module_id):
    module = get_object_or_404(Module, pk = module_id)
    ques_code = module.qcode
    questions = Question.objects.order_by('-q_date').filter(code=ques_code)
    context = {
        'module' : module,
        'questions' : questions,
    }
    return render(request,'modules/module.html',context)
