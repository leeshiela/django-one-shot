from django.shortcuts import render, get_object_or_404, redirect
from todos.models import ToDoList
from todos.forms import ToDoForm

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

def todo_list_create(request):
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            list = form.save()
            return redirect("todo_list_detail", id=list.id)
    else:
        form = ToDoForm()
    context= {
        "form": form,
    }
    return render(request, "todos/todo_list_create.html", context)
