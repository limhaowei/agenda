from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.

def index(request):
    task_list = Task.objects.order_by("-deadline")
    return render(request, 'base.html', {'task_list' : task_list})

def remove(request)