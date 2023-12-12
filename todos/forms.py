from django import forms
from todos.models import ToDoList

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = [
            "name",
        ]
