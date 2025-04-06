# core/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="No description")
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    student_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.username