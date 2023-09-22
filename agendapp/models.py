from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=200)
    desc = models.TextField()
    deadline = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.task 