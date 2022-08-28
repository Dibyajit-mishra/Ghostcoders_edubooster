from django.db import models

# Create your models here.
class User(models.Model):
    Task = models.CharField(max_length=80)
    description = models.TextField()