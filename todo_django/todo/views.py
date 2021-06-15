from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .forms import UserSignupForm, TaskCreateForm, TaskEditForm
from .models import *
import datetime


def index(request):
  url = 'login'
  if request.user.is_authenticated:
    url = 'home'
  return redirect(url)


def signup(request):
  if request.method == 'POST':
    form = UserSignupForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data['username']
      messages.success(request, f'The user {username} was created.')
  else:
    form = UserSignupForm()
  context = {
    'form': form,
  }
  return render(request, 'signup.html', context)


def login(request):
  return render(request, 'login.html')


def home(request):
  if not request.user.is_authenticated:
    return redirect('login')
  current_user = get_object_or_404(User, pk=request.user.pk)
  query = Q(user_id = current_user.pk)
  tasks = Task.objects.filter(user_id = current_user.pk, ended_at=None, expired_at__gte=datetime.datetime.now())
  context = {
    'tasks': tasks,
    'add_task_form': TaskCreateForm(),
    'edit_task_form': TaskEditForm(),
    'user': current_user,
  }
  return render(request, 'home.html', context)


def ended_tasks(request):
  if not request.user.is_authenticated:
    return redirect('login')
  current_user = get_object_or_404(User, pk=request.user.pk)
  query = ~Q(ended_at = None)
  query.add(Q(expired_at__lte=datetime.datetime.now()), Q.OR)
  query.add(Q(user_id = current_user.pk), Q.AND)
  tasks = Task.objects.filter(query)
  context = {
    'tasks': tasks,
    'user': current_user,
  }
  return render(request, 'ended-tasks.html', context)

def all_tasks(request):
  if not request.user.is_authenticated:
    return redirect('login')
  current_user = get_object_or_404(User, pk=request.user.pk)
  tasks = Task.objects.all()
  context = {
    'tasks': tasks,
    'user': current_user,
  }
  return render(request, 'all-tasks.html', context)


def user_edit(request):
  return render(request, 'login.html')


def add_task(request):
  if request.method == 'POST' and request.user.is_authenticated:
    current_user = get_object_or_404(User, pk=request.user.pk)
    form = TaskCreateForm(request.POST)
    if form.is_valid():
      title = form.cleaned_data['title']
      task = form.save(commit=False)
      task.user = current_user
      task.save()
      messages.success(request, f'The task {title} was created.')
  return redirect('home')


def task_edit(request):
  if request.method == 'POST' and request.user.is_authenticated:
    task_id = request.POST.get('task')
    instance = get_object_or_404(Task, pk=task_id)
    form = TaskEditForm(request.POST, instance=instance)
    if form.is_valid():
      title = form.cleaned_data['title']
      form.save()
      messages.success(request, f'The task {title} was updated.')
  return redirect('home')


def task_end(request, task_id):
  if request.user.is_authenticated:
    task = get_object_or_404(Task, pk=task_id)
    task.ended_at = datetime.datetime.now()
    task.save()
    messages.success(request, f'The task {task.title} was ended.')
  return redirect('home')


def task_delete(request, task_id):
  if request.user.is_authenticated:
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    messages.success(request, f'The task {task.title} was deleted.')
  return redirect('home')
