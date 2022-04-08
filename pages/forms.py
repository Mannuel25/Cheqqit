from django import forms
from .models import UserTasks

class AddTaskForm(forms.ModelForm):
    """
    this form will be used to create or update a task
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
        fields = ('title', 'description','task_due_date','task_due_time',)

class UpdateTaskForm(forms.ModelForm):
    """
    this form will be used to update the task created
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
    completed_task = forms.BooleanField(label='Completed this task?',
        required = False, widget=forms.widgets.CheckboxInput(attrs={'class': 'checkbox-inline'}),
    )
    
    class Meta(forms.ModelForm):
        model = UserTasks
        fields = ('title', 'description','task_due_date','task_due_time', 'completed_task',)

class TaskDetailsForm(forms.ModelForm):
    """
    this form will be used to view the task created
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
        fields = ('title', 'description','task_due_date','task_due_time',)

class TaskPositionForm(forms.Form):
    task_position = forms.CharField()