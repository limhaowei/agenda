from django.contrib import admin
from .models import Task
# Register your models here.

class AgendaAdmin(admin.ModelAdmin):
    list_display = ("task", "deadline", "days_left")


admin.site.register(Task, AgendaAdmin)
