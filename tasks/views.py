from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import Task
from .forms import TaskForm

def home(request):
    context = {}
    return render(request, 'tasks/home.html', context)

def tasks(request):
    tasks = Task.objects.all()
    form = TaskForm()

    context = {'tasks':tasks, 'form':form}

    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("") 

    return render(request, 'tasks/tasks.html', context)

def editTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method=='POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')

    context = {'form': form}
    return render(request, 'tasks/edit_task.html', context)

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method=='POST':
        task.delete()
        return redirect('tasks')

    context = {'task': task}
    return render(request, 'tasks/delete_task.html', context)

def notes(request):
    context = {}
    return render(request, 'tasks/notes.html', context)

def accounts(request):
    context = {}
    return render(request, 'tasks/accounts.html', context)
