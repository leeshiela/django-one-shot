from django.contrib import admin
from todos.models import ToDoList, ToDoItem

@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "id",
    ]

@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = [
        "task",
        "due_date",
        "is_completed",
    ]
