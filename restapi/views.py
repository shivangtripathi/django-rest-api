from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TodosSerializers
# Create your views here.
from .models import Todos

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'List':'/task-list',
        'Create':'/task-create',
        'Details':'/task-detail/<str:pk>',
        'Update':'/task-update/<str:pk>',
        'Delete':'/task-delete/<str:pk>',
    }
    return Response(api_urls)

# List all endpoints
@api_view(['GET'])
def todosList(request):
    todos = Todos.objects.all()
    serializer = TodosSerializers(todos,many=True)
    return Response(serializer.data)

#List task detail
@api_view(['GET'])
def todosDetail(request,pk):
    todo = Todos.objects.get(id=pk)
    serializer = TodosSerializers(todo,many=False)
    return Response(serializer.data)

#Task add
@api_view(['POST'])
def todosAdd(request):
    serializer = TodosSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#Task update
@api_view(['POST'])
def todosUpdate(request,pk):
    todo = Todos.objects.get(id=pk)
    serializer = TodosSerializers(instance=todo,data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

#Task Delete
@api_view(['DELETE'])
def todosDelete(request,pk):
    todo = Todos.objects.get(id=pk)
    todo.delete()
    return Response("Item Deleted Successfully !")