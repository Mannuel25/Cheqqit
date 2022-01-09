from django import forms
from .models import UserTasks

class TaskDetailsForm(forms.ModelForm):
    """
    this form will be used to either create a task/goal 
    or update the task/goal created
    """
    title = forms.CharField(max_length=100, widget= forms.TextInput
        (attrs={'placeholder':"Enter the task's title"}))
    description = forms.CharField(max_length=150, required=False, widget= forms.Textarea
        (attrs={'placeholder':"Enter the task's description"}))
    task_due_date = forms.DateField(
        label="Select the task's due date", required=False,
        widget=forms.widgets.DateInput(attrs={'type':'date'})
    )
    task_due_time = forms.TimeField(
        label="Select the task's due time", required=False,
        widget=forms.widgets.TimeInput(attrs={'type':'time'})
    )

    class Meta(forms.ModelForm):
        model = UserTasks
        fields = ('title', 'description','completed_task','task_due_date','task_due_time',)

class ViewTaskDetailsForm(forms.ModelForm):
    """
    this form will be used to only view the task/goal created
    """
    title = forms.CharField(max_length=100, label="Task's title",
        required=False, widget= forms.TextInput(attrs={'readonly':'readonly'}))
    description = forms.CharField(label="Task's description", 
        required=False, widget= forms.Textarea(attrs={'readonly':'readonly'}))
    task_due_date = forms.DateField(
        label="Task's due date", required=False,
        widget=forms.widgets.DateInput(attrs={'type':'date','readonly':'readonly'})
    )
    task_due_time = forms.TimeField(
        label="Task's due time", required=False,
        widget=forms.widgets.TimeInput(attrs={'type':'time','readonly':'readonly'})
    )

    class Meta(forms.ModelForm):
        model = UserTasks
        fields = ('title', 'description','completed_task','task_due_date','task_due_time',)
        