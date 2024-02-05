from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)