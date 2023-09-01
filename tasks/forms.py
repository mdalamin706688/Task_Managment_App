from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    due_date = forms.DateTimeField(required=False, widget=forms.TextInput(attrs={'type': 'datetime-local'}))
    priority = forms.IntegerField(min_value=0, max_value=8)

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'completed', 'categories']
