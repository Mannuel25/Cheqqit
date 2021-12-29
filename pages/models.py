from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
import string, random


def generate_random_slug():
    return ''.join(random.choice(string.digits) for _ in range(8))

class UserTasks(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed_task = models.BooleanField(default=False)
    task_due_date = models.DateField(null=True, blank=True)
    task_due_time = models.TimeField(null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    
    def __str__(self):
        return self.title
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + '-' + generate_random_slug())
        super(UserTasks, self).save(*args, **kwargs)
    
    class Meta:
        order_with_respect_to = 'user'