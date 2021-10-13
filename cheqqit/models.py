from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
  email = models.EmailField(max_length=254)