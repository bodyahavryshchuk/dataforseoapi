from django.contrib import admin

from src.tasks.models import Task, TaskData, TaskResult


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'status_code', 'status_message']
    list_filter = ['status_code', 'status_message']
    search_fields = ['id']


@admin.register(TaskData)
class TaskDataAdmin(admin.ModelAdmin):
    list_display = ['task', 'keyword']


@admin.register(TaskResult)
class TaskResultAdmin(admin.ModelAdmin):
    list_display = ['task']




