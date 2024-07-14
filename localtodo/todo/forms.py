from django.forms import ModelForm
from django import forms
from todo.models import ToDoItem

class ToDoForm(ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['content','due_date','is_completed']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})  # HTML5 input type
        }
