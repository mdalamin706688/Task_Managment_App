from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField(blank=True, null=True)
    priority = models.PositiveIntegerField(default=0)
    completed = models.BooleanField(default=False)
    categories = models.CharField(max_length=100, blank=True, null=True)  # CharField for categories

    def __str__(self):
        return self.title
