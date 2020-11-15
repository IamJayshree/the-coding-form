from django.shortcuts import render, redirect
from django.http import HttpResponse
from subprocess import run, PIPE
from django.core.files import File 
from django.contrib  import messages, auth
from .utils import compileCpp, compileJava, compilePy

def index(request):
    if(request.method == 'POST'):
        code = request.POST['aesteditor']
        language = request.POST['lang']
        inputdata = request.POST['inputbox']

        if not code:
           messages.error(request,'Code Editor was empty')
           return render(request, 'pages/index.html') 
            
        if(language == '0'):
           messages.error(request,'No Language Selected')
           return render(request, 'pages/index.html')

        if(language == '1'):
            data = {
                'code' : code,
                'inputdata' : inputdata,
            }
            outputdata = compileCpp(data)


        if(language == '2'):
            data = {
                'code' : code,
                'inputdata' : inputdata,
            }
            outputdata = compileJava(data) 

        if(language == '3'):
            data = {
                'code' : code,
                'inputdata' : inputdata,
            }
            outputdata = compilePy(data) 
            

        context = {
            'code' : code,
            'language' : language,
            'inputdata' : inputdata,
            'outputdata' : outputdata
        }

            
        return render(request, 'pages/index.html',context)
    return render(request, 'pages/index.html')


