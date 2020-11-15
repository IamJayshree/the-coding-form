from django.shortcuts import render, redirect
from django.http import HttpResponse
from subprocess import run, PIPE
from django.core.files import File 
from django.contrib  import messages, auth

def compileCpp(data):
    code = data['code']
    inputdata = data['inputdata']
    inputs = inputdata.encode('utf-8')
    f1 = open('data.cpp','w')
    f1.write(code)
    f1.close()
    var = "data.cpp"
    p0 = run(["g++","-o","a",var],input=inputs,stderr=PIPE,stdout=PIPE)

    if p0.returncode == 0:
        output = run(["./a"],stderr=PIPE,stdout=PIPE)
        outputdata = output.stdout.decode('utf-8')
    # run(["g++","-o","a",var])
    # output = run(['./a'], stdout=PIPE)
    else:
        outputdata = p0.stderr.decode('utf-8')
    return outputdata
    

def compileJava(data):
    code = data['code']
    inputdata = data['inputdata']
    inputs = inputdata.encode('utf-8')
    f1 = open('solve.java','w')
    f1.write(code)
    f1.close()
    var = "solve.java"
    run(["javac",var])
    outputdata = run(["java","solve"],input=inputs,stdout=PIPE).stdout.decode('utf-8')
    return outputdata

def compilePy(data):
    code = data['code']
    f1 = open('file.py','w')
    inputdata = data['inputdata']
    inputs = inputdata.encode('utf-8')
    f1.write(code)
    f1.close()
    var = "file.py"
    outputdata = run(['python3',var],input=inputs,stdout=PIPE).stdout.decode('utf-8')
    return outputdata