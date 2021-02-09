from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import TaskSerializer
from . models import Task


# Create your views here.
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def task(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)  


@api_view(['POST'])
def createTask(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)  

@api_view(['DELETE'])
def deleteTask(request, pk):
    task= Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    task.delete()
    return Response(serializer.data)

