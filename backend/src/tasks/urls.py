from django.urls import path

from . import views

urlpatterns = [
    path("task/", views.TaskCreateView.as_view(), name='task_create'),
    path("task-list/", views.TaskListView.as_view(), name='task_list'),
    path("task/data/", views.TaskDataListView.as_view(), name='task_data'),
    path("task/result/<str:se>/<str:pk>/", views.TaskResultListView.as_view(), name='task_result'),
]
