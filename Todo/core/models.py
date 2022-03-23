from datetime import datetime
from statistics import mode
import django
from django.db import models

# Create your models here.


class Todo(models.Model):
    todo = models.CharField(max_length=255, null=False, blank=False, verbose_name='Todo')
    status = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='images/', null=True, blank=True, default='images/default.jpg')
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.todo

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)