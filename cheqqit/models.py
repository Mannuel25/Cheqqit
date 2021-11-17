from django.contrib.auth.models import User, AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=20,unique=True)
    email = models.EmailField(max_length=70,unique=True)
    password = models.CharField(max_length=12)

class Tasks(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed_task = models.BooleanField(default=False)
    task_created_when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'
