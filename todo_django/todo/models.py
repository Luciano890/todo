from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default='/images/avatar.jpg')
  def __str__(self):
    return self.user.username
  

class Category(models.Model):
  name = models.CharField(max_length=100)
  image = models.CharField(max_length=255)
  def __str__(self):
    return self.name


class Task(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=150, null=True)
  expired_at = models.DateTimeField()
  ended_at = models.DateTimeField(null=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
  
  class Meta:
    ordering = ['expired_at']

  def __str__(self):
    return self.title
