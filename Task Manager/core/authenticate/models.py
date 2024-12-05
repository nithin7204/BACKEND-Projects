from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.TextField()
    completed = models.BooleanField()
    time = models.DateTimeField(auto_now_add = True)
