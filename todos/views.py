from django.shortcuts import render, get_object_or_404
from todos.models import ToDoList

def todo_list_list(request):
    todos = ToDoList.objects.all()
    context = {
        "todos_list": todos,
    }
    return render(request, "todos/todos.html", context)

def todo_list_detail(request, id):
    todo_list = get_object_or_404(ToDoList, id=id)
    context = {
        "todo_list": todo_list,
    }
    return render(request, "todos/todo_detail.html", context)
