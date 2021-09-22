import datetime
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='uploads/')
    discription = models.CharField(max_length=5000)
    date = models.DateField(default=datetime.datetime.today)


class Users(models.Model):
    nickname = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/')
    created = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    blog = models.ForeignKey('Blog', related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Reply_comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comment_id = models.ForeignKey('Comment', related_name='replies', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']