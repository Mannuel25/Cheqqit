from django.db import models
from django.contrib.auth import get_user_model

class UserTasks(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed_task = models.BooleanField(default=False)
    task_created_when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
<<<<<<< HEAD
        order_with_respect_to = 'user'
=======
        order_with_respect_to = 'user'
>>>>>>> 3a17f8703de8f1689401ca6490478e9e80bff593
