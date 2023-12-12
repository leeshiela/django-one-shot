from django.contrib import admin
from todos.models import ToDoList

@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "id",
    ]
