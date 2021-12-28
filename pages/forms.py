from django import forms
from .models import UserTasks

class TaskDetails(forms.ModelForm):
    title = forms.CharField(max_length=100, widget= forms.TextInput
        (attrs={'placeholder':"Enter task/goal's title"}))
    description = forms.CharField(max_length=150, required=False, widget= forms.Textarea
        (attrs={'placeholder':"Enter task/goal's description"}))
    task_due_date = forms.DateField(
        label="Select task/goal's due date", required=False,
        widget=forms.widgets.DateInput(attrs={'type':'date'})
    )
    task_due_time = forms.TimeField(
        label="Select task/goal's due time", required=False,
        widget=forms.widgets.TimeInput(attrs={'type':'time'})
    )

    class Meta(forms.ModelForm):
        model = UserTasks
        fields = ('title', 'description','completed_task','task_due_date','task_due_time',)