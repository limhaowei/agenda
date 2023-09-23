from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    task = models.TextField()
    deadline = models.DateTimeField(default=timezone.now)

    def days_left(self):
        now = timezone.now()
        if self.deadline >= now:
            delta = self.deadline - now
            return delta.days
        else:
            return 0 


    def __str__(self):
        return self.task 
