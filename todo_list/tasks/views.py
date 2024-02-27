from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect
from tasks.models import Task
from tasks.forms import TaskForm


@login_required
def task_list(request):
    tasks = Task.objects.filter(user__id=request.user.id)
    search_input = request.GET.get('search-area')
    if search_input:
        tasks = tasks.filter(title__icontains=search_input)
    return render(request, 'tasks/tasks.html', {'tasks': tasks, 'search_input': search_input})


@login_required
def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'tasks/task.html', {'task': task})


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect(reverse('tasks:tasklist'))
    else:
        form = TaskForm()

    context = {
        'title': 'ToDo - создать',
        'form': form
    }
    return render(request, 'tasks/task_form.html', context)


@login_required
def task_update(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(request.POST or None, instance=task)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('tasks:tasklist'))

    context = {
        'title': 'ToDo - изменить',
        'form': form
    }
    return render(request, 'tasks/task_form.html', context)


@login_required
def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST' and task:
        task.delete()
    else:
        return render(request, 'tasks/task_delete.html')
    return redirect(reverse('tasks:tasklist'))
