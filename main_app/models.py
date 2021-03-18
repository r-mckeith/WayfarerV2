from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class City(models.Model):
  name = models.CharField(max_length=100, unique=True)
  photo_url = models.CharField(max_length=500)

  def __str__(self):
    return self.name

class Post(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField(max_length=500)
  created_at = models.DateTimeField(auto_now_add=True)
  city = models.ForeignKey(City, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.title}, {self.city}'

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  current_city = models.CharField(max_length=50)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)

  def __str__(self):
    return f'{self.first_name} {self.last_name} is from {self.current_city}'