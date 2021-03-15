from django.db import models

# Create your models here.
class City(models.Model):
  name = models.CharField(max_length=100, unique=True)

  def __str__(self):
    return self.name

class Post(models.Model):
  title = models.CharField(max_length=100)
  body = models.TextField(max_length=500)
  city = models.ForeignKey(City, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.title}, {self.city}'