from django.contrib.auth.models import User
from django.db import models

class ToDo(models.Model):
    """
    purpose: Creates ToDo instance within database        

    author: Taylor Perkins

    args: models.Model: (NA): models class given by Django

    returns: (None): N/A
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    description = models.TextField(blank=False, null=False, max_length=1000)
