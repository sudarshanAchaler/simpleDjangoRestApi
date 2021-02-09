from django.urls import path
from . views import taskList, task, createTask, deleteTask
urlpatterns = [
    path('taskList/', taskList, name='taskList'),
    path('taskList/<str:pk>/', task, name='task'),
    path('createTask/', createTask , name='createTask'),
    path('deleteTask/<str:pk>/', deleteTask , name='deleteTask'),
]