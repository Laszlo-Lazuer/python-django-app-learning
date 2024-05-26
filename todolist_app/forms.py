from django import forms
from todolist_app.models import TaskList # DB

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['task', 'done']

