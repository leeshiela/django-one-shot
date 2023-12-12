from django.shortcuts import render
from todos.models import ToDoList

def todo_list_list(request):
    todos = ToDoList.objects.all()
    context = {
        "todos_list": todos,
    }
    return render(request, "todos/todos.html", context)
