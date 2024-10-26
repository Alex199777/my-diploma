from django.db import models

# Create your models here.
class CoverImage(models.Model):
    image = models.FileField(upload_to='img/')

