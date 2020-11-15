from django.shortcuts import render, redirect
from django.contrib  import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from modules.models import Module

def login(request):
     if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = auth.authenticate(username=username, password=password)
          if user is not None:
               auth.login(request,user)
               messages.success(request,'You are now logged in')
               return redirect('home')
          else:
               messages.error(request,'Invalid Credentials')
               return redirect('login')
     else:
          return render(request,'accounts/login.html')

def logout(request):
     if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
     return redirect('home')

def register(request):
     if request.method == 'POST':
          #GET FORM VALUES
          username = request.POST['username']
          password = request.POST['password']
          password2 = request.POST['password2']
     #Check if passwords match
          if password == password2:
               #check username
               if User.objects.filter(username=username).exists():
                    messages.error(request,'That username is being used')
                    # return redirect('register')
                    # return render(request, 'modules/home.html')
                    return redirect('home')
               else:
                    #looks good
                    user = User.objects.create_user(username=username, password=password)
                    user.save()
                    messages.success(request,'You are now registered and can login')
                    return redirect('login')
          else:
               messages.error(request,'Passwords do not match')
               return redirect('register')
     else:
          return render(request, 'accounts/register.html')

def home(request):
    modules = Module.objects.order_by('-mod_date').filter(is_Published=True)
    paginator = Paginator(modules, 6)
    page = request.GET.get('page')
    paged_modules = paginator.get_page(page)
    context = {
        'modules' : paged_modules
    }
    return render(request,'modules/home.html',context)   


def dashboard(request):
     return render(request, 'accounts/dashboard.html')
 

