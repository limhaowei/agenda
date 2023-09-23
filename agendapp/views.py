from django.shortcuts import render

from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task

# Create your views here.

def index(request):
    return HttpResponse("im super shy")


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()   
