from django import forms
from .models import UserTasks

class TaskDetails(forms.ModelForm):
    title = forms.CharField(max_length=100, widget= forms.TextInput
        (attrs={'placeholder':'Enter the task/goal title'}))
    description = forms.CharField(max_length=150, required=False, widget= forms.Textarea
        (attrs={'placeholder':'Enter the task/goal description'}))

    class Meta(forms.ModelForm):
        model = UserTasks
        fields = ('title', 'description','completed_task',)
