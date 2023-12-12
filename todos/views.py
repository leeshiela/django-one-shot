from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList
from todos.forms import TodoForm

def todo_list_list(request):
    todos = TodoList.objects.all()
    context = {
        "todos_list": todos,
    }
    return render(request, "todos/todos.html", context)

def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    context = {
        "todo_list": todo_list,
    }
    return render(request, "todos/todo_detail.html", context)

def todo_list_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            list = form.save()
            return redirect("todo_list_detail", id=list.id)
    else:
        form = TodoForm()
    context= {
        "form": form,
    }
    return render(request, "todos/todo_list_create.html", context)

def todo_list_update(request, id):
    post = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("todo_list_detail", id=id)
    else:
        form = TodoForm(instance=post)
    context = {
        "todo_list": post,
        "todo_form": form,
    }
    return render(request, "todos/todo_edit.html", context)

def todo_list_delete(request, id):
    post = TodoList.objects.get(id=id)
    if request.method == "POST":
        post.delete()
        return redirect("todo_list_list")

    return render(request, "todos/todo_delete.html")
