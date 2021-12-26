from django.db import models
from django.contrib.auth import get_user_model

class UserTasks(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed_task = models.BooleanField(default=False)
    task_due_date = models.DateField(null=True, blank=True)
    task_due_time = models.TimeField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        order_with_respect_to = 'user'