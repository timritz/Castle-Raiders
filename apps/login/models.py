from __future__ import unicode_literals
from django.db import models

class Player(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length= 255)
    characterType = models.CharField(max_length=255)
    status=models.CharField(max_length=255)
