from django.shortcuts import render, redirect

from .models import Task
from .forms import TaskForm


def index(request) :
    tasks = Task.objects.order_by('-id')[:5]    # [:5] - срез, т.е. всего 5 записей
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})   # 'main/index.html' - как-будто уже находишься в папке templates

def about(request):
    return render(request, 'main/about.html')   # 'main/index.html' - как-будто уже находишься в папке templates

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Форма была некорректна'

    form = TaskForm()
    context = {
        'title': 'Добавить задачу',
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)