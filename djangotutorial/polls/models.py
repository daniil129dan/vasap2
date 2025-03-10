import datetime

from django.db import models
from django.utils import timezone

class Roles(models.TextChoices):
    USER = 'user', 'User'
    ADMIN = 'admin', 'Admin'

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password_hash = models.CharField(max_length=64)
    role = models.CharField(
        max_length=50,
        choices=Roles.choices,
        default="User",
    )