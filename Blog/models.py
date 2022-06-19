from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
from django.db import models

class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField('Hello world')
    Author = get_user_model()
    Created_date = models.DateTimeField('date published')
    Published_date = models.DateTimeField('date published')
    
