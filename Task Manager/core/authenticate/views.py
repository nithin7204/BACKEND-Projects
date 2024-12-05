from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Task
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,"home_page.html")

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('view_task')

def modify_task(request,id):
    task = get_object_or_404(Task, id=id)
    task.completed = not task.completed
    task.save()

    return redirect('view_task')

@login_required
def add_task(request):
    if request.method == 'POST':
        desc = request.POST.get('desc')

        task = Task(user=request.user,desc=desc,completed=False)
        task.save()

        return redirect('view_task')
    return render(request,"add_task.html")


@login_required
def view_task(request):
    tasks = Task.objects.filter(user = request.user)

    context = {'tasks':tasks}

    return render(request,"view_task.html",context)

def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        name = request.POST.get('name')

        User.objects.create_user(username=username,password=password,email=email,first_name =name)

        new_user = authenticate(username=username, password=password)
        if new_user:
            login(request, new_user)
        
        return redirect('view_task')
    
    return render(request,"sign_up.html")

def login_user(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username , password=password)

        if user is not None:
            login(request,user)
            return redirect('view_task')
        else:
            return render(request,"error.html")
        
    return render(request,"login_page.html")

