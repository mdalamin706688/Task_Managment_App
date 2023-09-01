#task/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout  # Rename the imported logout function



@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            form.save_m2m()  # Save many-to-many relationships (categories)
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/edit_task.html', {'form': form})

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(request, 'tasks/confirm_delete.html', {'task': task})


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)

    # Sorting tasks based on query parameters
    sort_by = request.GET.get('sort_by')
    if sort_by == 'due_date':
        tasks = tasks.order_by('due_date')
    elif sort_by == 'priority':
        tasks = tasks.order_by('priority')
    elif sort_by == 'category':
        tasks = tasks.order_by('categories')

    # Filtering tasks based on query parameters
    filter_category = request.GET.get('category')
    if filter_category:
        tasks = tasks.filter(categories=filter_category)

    # Fetch the list of available categories for filtering options
    available_categories = Task.objects.filter(user=request.user).values_list('categories', flat=True).distinct()

    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'available_categories': available_categories})


@login_required
def custom_logout(request):
    auth_logout(request)
    return redirect('login')