from cmath import phase
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.
def index(request):
    sentence = 'Sentence from views.py'
    return render(request, 'index.html', {
        'sentence': sentence,
    })


def hello(request, username):
    return HttpResponse(f'Hello {username}')


def about(request):
    return HttpResponse('About')

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def task(request, id):
    tasks = get_object_or_404(Task, pk=id)
    return JsonResponse(tasks.name, safe=False)

def tasks(request):
    tasks = list(Task.objects.values())
    return JsonResponse(tasks, safe=False)