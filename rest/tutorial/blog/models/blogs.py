from django.db import models
import datetime


class Blogs(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/')
    description = models.CharField(default='', max_length=2000)
    date = models.DateField(default=datetime.datetime.today)