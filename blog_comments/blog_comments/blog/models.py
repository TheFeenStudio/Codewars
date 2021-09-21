import datetime
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='uploads/')
    discription = models.CharField(max_length=5000)
    date = models.DateField(default=datetime.datetime.today)