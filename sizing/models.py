from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Body(models.Model):
    height = models.IntegerField()
    bodyImage = models.ImageField(upload_to = 'images/')