from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib import messages
from .models import Task

from .forms import TaskForm

# def my_view(request):
#     return HttpResponse("belajar crud")

def index_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks' : tasks
    }
    return render(request, 'todo/index.html', context)

def detail_view(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        context = {
            'task': task
        }
    except Task.DoesNotExist:
        raise Http404("Task not found")
    return render(request, 'todo/detail.html', context)

def create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sukses menambahkan task baru')
            return redirect('todo:index')
    else:
        form = TaskForm()
    return render(request, 'todo/form.html', {'form': form})

def update_view(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task not found")

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sukses memperbarui task')
            return redirect('todo:index')
    else:
        form = TaskForm(instance=task)

    return render(request, 'todo/form.html', {'form': form})