from django.db import models

# Create your models here.

class MapModel(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  image = models.ImageField(upload_to="")
  def __str__(self):
    return self.title

