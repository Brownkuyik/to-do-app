from django.db import models
from django.urls import reverse

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=300, unique=True)
    description = models.TextField(max_length=520, blank=True, null=True)
    is_done = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("TodoApp:task-details", args=[self.id])

    def __str__(self):
        return f'Task #{self.id}'
