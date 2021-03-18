from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone
import math

# Create your models here.
class City(models.Model):
  name = models.CharField(max_length=100, unique=True)
  photo_url = models.CharField(max_length=500)
  slug = models.SlugField(max_length=50, blank=True)

  def save(self):
    if not self.id: 
      self.slug = slugify(self.name)
    super(City, self).save()


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

  def posted(self):
    now = timezone.now()
    created_at = models.DateTimeField(auto_now_add=True)
    difference = now - self.created_at
    
    if difference.days == 0 and difference.seconds >= 0 and difference.seconds <= 60:
      return 'just now'
    elif difference.days == 0 and difference.seconds >= 60 and difference.seconds < 3600:
      minutes = math.floor(difference.seconds/60)
      if minutes == 1:
        return '1 minute ago'
      else:
        return str(minutes) + 'minutes ago'
    elif difference.days == 0 and difference.seconds >= 3600 and difference.seconds < 86400:
      hours = math.floor(difference.seconds/3600)
      if hours == 1:
        return '1 hour ago'
      else: 
        return str(hours) + 'hours ago'
    elif difference.days >= 1 and difference.days < 30:
      days = difference.days
      if days == 1:
        return '1 day ago'
      else: 
        return str(days) + 'days ago'
    elif difference.days >= 30 and difference.days < 365:
      months = math.floor(difference.days/30)
      if months == 1:
        return str(months) + 'month ago'
      else:
        return str(months) + 'months ago'
    else:
      years = math.floor(difference.days/365)
      if years == 1:
        return '1 year ago'
      else:
        return str(years) + 'years ago'

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  content = models.TextField()

  def __str__(self):
    return f'{self.user}\'s comment'

  def posted(self):
    now = timezone.now()
    created_at = models.DateTimeField(auto_now_add=True)
    difference = now - self.created_at
    
    if difference.days == 0 and difference.seconds >= 0 and difference.seconds <= 60:
      return 'just now'
    elif difference.days == 0 and difference.seconds >= 60 and difference.seconds < 3600:
      minutes = math.floor(difference.seconds/60)
      if minutes == 1:
        return '1 minute ago'
      else:
        return str(minutes) + ' minutes ago'
    elif difference.days == 0 and difference.seconds >= 3600 and difference.seconds < 86400:
      hours = math.floor(difference.seconds/3600)
      if hours == 1:
        return '1 hour ago'
      else: 
        return str(hours) + ' hours ago'
    elif difference.days >= 1 and difference.days < 30:
      days = difference.days
      if days == 1:
        return '1 day ago'
      else: 
        return str(days) + ' days ago'
    elif difference.days >= 30 and difference.days < 365:
      months = math.floor(difference.days/30)
      if months == 1:
        return str(months) + ' month ago'
      else:
        return str(months) + ' months ago'
    else:
      years = math.floor(difference.days/365)
      if years == 1:
        return '1 year ago'
      else:
        return str(years) + ' years ago'

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  current_city = models.CharField(max_length=50)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)

  def __str__(self):
    return f'{self.first_name} {self.last_name} is from {self.current_city}'